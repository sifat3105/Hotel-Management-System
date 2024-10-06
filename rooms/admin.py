from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import Room
from bookings.models import Booking
from django.utils import timezone
from django.contrib.admin import SimpleListFilter
from datetime import timedelta
from django.utils.html import format_html

class BookedRoomFilter(SimpleListFilter):
    title = 'Booked status'
    parameter_name = 'is_booked'

    def lookups(self, request, model_admin):
        return (
            ('booked', 'Booked'),
            ('available', 'Available'),
        )

    def queryset(self, request, queryset):
        today = timezone.now().date()
        if self.value() == 'booked':
            return queryset.filter(booking__check_in__lte=today, booking__check_out__gte=today).distinct()
        if self.value() == 'available':
            return queryset.exclude(booking__check_in__lte=today, booking__check_out__gte=today).distinct()

class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'room_number', 'room_type', 'price', 'is_available', 
        'is_booked', 'beds', 'baths', 'max_adults', 'max_children', 
        'current_booking_dates', 'view_available_days'
    )
    search_fields = ('room_number', 'room_type')
    list_filter = ('room_type', 'is_available', BookedRoomFilter) 
    ordering = ('room_number',)
    
    def is_booked(self, obj):
        today = timezone.now().date()
        return Booking.objects.filter(room=obj, check_in__lte=today, check_out__gte=today).exists()
    is_booked.boolean = True  # Display as boolean
    is_booked.short_description = 'Booked'

    def current_booking_dates(self, obj):
        today = timezone.now().date()
        booking = Booking.objects.filter(room=obj, check_in__lte=today, check_out__gte=today).first()
        if booking:
            return f"{booking.check_in} to {booking.check_out}"
        return "No current booking"

    def view_available_days(self, obj):
        return format_html('<a href="{}">View Available Days</a>', 
                       f"/admin/{obj._meta.app_label}/{obj._meta.model_name}/{obj.pk}/available-days/")
    view_available_days.short_description = 'Available Days'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:room_id>/available-days/',
                self.admin_site.admin_view(self.available_days_view),
                name='room_available_days',
            ),
        ]
        return custom_urls + urls

    def available_days_view(self, request, room_id, *args, **kwargs):
        room = self.get_object(request, room_id)
        today = timezone.now().date()
        dates = []
        
        # Check availability for the next 20 days
        for i in range(31):  # Today + next 20 days
            date = today + timedelta(days=i)
            booked = Booking.objects.filter(room=room, check_in__lte=date, check_out__gte=date).exists()
            dates.append({
                'date': date.strftime("%Y-%m-%d"),
                'available': not booked
            })
        
        context = {
            'room': room,
            'dates': dates,
        }
        return render(request, 'admin/room_available_days.html', context)
    

admin.site.register(Room, RoomAdmin)
