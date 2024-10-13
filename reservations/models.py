from django.db import models

# Create your models here.

class Reservations(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    pnune_number = models.CharField(max_length=15)
    number_of_guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    special_occasions = models.CharField(max_length=200, blank = True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"