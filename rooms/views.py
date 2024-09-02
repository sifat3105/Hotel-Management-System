from django.shortcuts import render
from .models import Room

# Create your views here.


def available_rooms(request):
    available_rooms = Room.objects.filter(is_available=True)
    return render(request, 'rooms/available_rooms.html', {'rooms': available_rooms})