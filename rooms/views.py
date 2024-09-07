from django.shortcuts import render
from .models import Room
from datetime import date
from django.db.models import Q

def search_available_rooms(check_in, check_out, adults, children):
    
    rooms = Room.objects.filter(
        max_adults=adults, 
        max_children=children,
        is_available = True
    )

   

    return rooms


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