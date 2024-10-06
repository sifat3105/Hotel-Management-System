from django.db import models

class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]
    
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='rooms/', blank=True, null=True)
    beds = models.IntegerField(default=1)
    baths = models.IntegerField(default=1)
    max_adults = models.IntegerField(default=2)
    max_children = models.IntegerField(default=1)

    def __str__(self):
        return f"Room {self.room_number} ({self.get_room_type_display()})"
