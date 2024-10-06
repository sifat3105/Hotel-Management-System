from django.urls import path
from .views import available_rooms
urlpatterns = [
    path('rooms/', available_rooms, name='rooms'),
]

