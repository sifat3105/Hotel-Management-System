from django.db import models
from rooms.models import Room
from guests.models import Guest



class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f"Booking {self.id} - {self.guest} ({self.room})"