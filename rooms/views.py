from django.shortcuts import render
from .models import Room
from datetime import date
from django.db.models import Q
from bookings.models import Booking
from django.utils import timezone
from datetime import timedelta

def search_available_rooms(check_in, check_out, adults, children):
    booked_room_numbers = Booking.objects.filter(
        check_in__lt=check_out, 
        check_out__gt=check_in
    ).values_list('room__room_number', flat=True)

    # Filter for available rooms that meet the criteria
    available_rooms = Room.objects.filter(
        max_adults__gte=adults, 
        max_children__gte=children,
        
    ).exclude(room_number__in=booked_room_numbers)

    return available_rooms


def available_rooms(request):
    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        adults = request.POST.get('adult')
        children = request.POST.get('child')
        print(adults, children)
        rooms = search_available_rooms(check_in, check_out, adults, children)
    else:
        rooms = Room.objects.filter(is_available=True)
    return render(request, 'rooms.html', {'rooms': rooms})


