from django import forms

class ReservationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    date = forms.DateField(widget=forms.SelectDateWidget, label='Date')
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label='Time')
    number_of_guests = forms.IntegerField(min_value=1, label='Number of Guests')
    special_occasion = forms.CharField(max_length=200, required=False, label='Special Occasion')