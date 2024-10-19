from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    # shows the data as a list in the admin panel
    list_display = ('name', 'phone_number', 'number_of_guests', 'date', 'time', 'special_occasion')

    # Add filter for date
    list_filter = ('date', 'number_of_guests')

# Register the model and the custom admin class
admin.site.register(Reservation, ReservationAdmin)