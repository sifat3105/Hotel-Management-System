from django.shortcuts import render
from rooms.models import Room
from guests.models import Guest
# Create your views here.

def home_view (request):
    rooms = Room.objects.all()
    total_clint = Guest.objects.count()
    total_rooms = Room.objects.count()
    context={
        'rooms':rooms,
        'total_clint':total_clint,
        'total_rooms':total_rooms,
    }
    
    
    return render(request, 'home.html', context)
