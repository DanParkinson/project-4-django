from django import forms

class ReservationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    date = forms.DateField(widget=forms.SelectDateWidget, label='Date')
    number_of_guests = forms.IntegerField(min_value=1, label='Number of Guests')
    special_occasion = forms.CharField(max_length=200, required=False, label='Special Occasion')

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