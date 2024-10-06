from django.db import models
from rooms.models import Room
from guests.models import Guest
from django.utils import timezone




class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_con = models.PositiveSmallIntegerField(default=1)
    check_in = models.DateField(default=timezone.now)
    check_out = models.DateField(null=True, blank= True)
    adults = models.IntegerField(default=1)
    children = models.IntegerField(default=0)
    paid = models.BooleanField(default= False)
    def __str__(self):
        return f"Booking for {self.room} from {self.check_in} to {self.check_out}"
