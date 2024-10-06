from django.urls import path
from .views import booking_view, selected_room_booking


urlpatterns = [
    path('', booking_view, name='booking'),
    path('room/<int:id>/', selected_room_booking, name='selected_room_booking')

]
