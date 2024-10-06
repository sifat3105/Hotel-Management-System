from django.shortcuts import render
from .models import Guest
# Create your views here.


def guest_create(first_name, last_name, email, number):
    guest, Created = Guest.objects.get_or_create(
        first_name = first_name,
        last_name = last_name,
        email = email,
        phone_number = number,
    )
    return guest