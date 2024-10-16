from django import forms
from django.utils import timezone
from .models import Reservation

class ReservationForm(forms.ModelForm):
    # Meta class to link the form to the Reservation model
    class Meta:
        model = Reservation  # Link the form to the Reservation model
        fields = ['name', 'email', 'phone_number', 'number_of_guests', 'date', 'time', 'special_occasion']

    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    number_of_guests = forms.IntegerField(min_value=1, label='Number of Guests', max_value=8)
    special_occasion = forms.CharField(max_length=200, required=False, label='Special Occasion')

    # set phone number to allow only numbers
    phone_number = forms.IntegerField(
        min_value=0,
        error_messages={'invalid' : 'Phone number must be number.'},
        label='Phone Number')

    # Set date to current day and onwards
    # get todays date
    today = timezone.now().date()

    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type':'date',
            'min': today # set the min date to current day
        }), 
        label='Date'
    )

    # creates 15 minute intervals for the time selection drop down within open hours
    TIME_CHOICES = [
        (f"{hour:02}:{minute:02}", f"{hour:02}:{minute:02}")
        for hour in range(10, 21) # 10am to 9pm
        for minute in (0, 15, 30, 45) # 15 minute intervals
    ]
    # The actual time data 
    time = forms.ChoiceField(
        # Limits users selecting out of hours reservations
        choices = TIME_CHOICES,
        label = 'Time'
         )