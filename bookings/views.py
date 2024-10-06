from django.shortcuts import render
from django.http import HttpResponse
from django.utils.dateparse import parse_date
from guests.views import guest_create
from rooms.views import search_available_rooms
from .models import Booking
from rooms.models import Room

def booking_view(request):
    if request.method == 'POST':
        # Collect data from POST request
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        number = request.POST.get('number')
        email = request.POST.get('email')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        adult = request.POST.get('adult')
        child = request.POST.get('child')
        room_com = request.POST.get('room')
        message = request.POST.get('message')
        
        # Manual validation using parse_date
        checkin_date = parse_date(checkin)
        checkout_date = parse_date(checkout)
        
        # Check if the dates are valid
        if not checkin_date or not checkout_date:
            return HttpResponse("Invalid date format. Please use YYYY-MM-DD.", status=400)

        rooms = search_available_rooms(checkin_date, checkout_date, adult, child)
        if rooms:
            room = min(rooms, key=lambda room: room.price)
            
            guest = guest_create(first_name, last_name, email, number)
            booking = Booking.objects.create(
                guest=guest,
                room=room,
                check_in=checkin_date,
                check_out=checkout_date,
                adults=adult,
                children=child,
                room_con=room_com,
            )
            room.is_available = False
            room.save()
        else:
            return render(request, "booking.html", {'error': 'Rooms not available'})
        return HttpResponse(f"Booking successful for {first_name}!")
    return render(request, "booking.html")



def selected_room_booking(request, id):
    if request.method == 'POST':
        # Collect data from POST request
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        number = request.POST.get('number')
        email = request.POST.get('email')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        adult = request.POST.get('adult')
        child = request.POST.get('child')
        room_com = request.POST.get('room')
        message = request.POST.get('message')
        
        # Manual validation using parse_date
        checkin_date = parse_date(checkin)
        checkout_date = parse_date(checkout)
        
        # Check if the dates are valid
        if not checkin_date or not checkout_date:
            return HttpResponse("Invalid date format. Please use YYYY-MM-DD.", status=400)

        room = Room.objects.get(id = id)
            
        guest = guest_create(first_name, last_name, email, number)
        booking = Booking.objects.create(
            guest=guest,
            room=room,
            check_in=checkin_date,
            check_out=checkout_date,
            adults=room.max_adults,
            children=room.max_children,
            room_con=1,
        )
        room.is_available = False
        room.save()
        return HttpResponse(f"Booking successful for {first_name}!")
    return render(request, "booking.html", {'selected_room':True})