from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('guest', 'room', 'check_in', 'check_out', 'adults', 'children', 'paid')
    search_fields = ('guest__name', 'room__name')
    list_filter = ('room', 'check_in', 'paid')
    ordering = ('-check_in',)
    change_form_template = 'admin/button.html'  # Ensure this is correct

admin.site.register(Booking, BookingAdmin)
