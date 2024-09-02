from django.shortcuts import render
from rooms.models import Room

# Create your views here.

def home_view (request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})
