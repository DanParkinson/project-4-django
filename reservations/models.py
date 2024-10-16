from django.db import models
from django.contrib.auth.models import User  # Import the User model

# Create your models here.
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User model
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    number_of_guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    special_occasion = models.CharField(max_length=200, blank = True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"