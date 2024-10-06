from django.db import models

class Staff(models.Model):
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('receptionist', 'Receptionist'),
        ('housekeeper', 'Housekeeper'),
        ('chef', 'Chef'),
        ('security', 'Security'),
        # Add more roles as needed
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_joined = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_role_display()}" 