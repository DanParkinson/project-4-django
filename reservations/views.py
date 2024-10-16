from django.contrib.auth.decorators import login_required # users must log in to reserve
from django.shortcuts import render
from .forms import ReservationForm # Imports form for reservation
from .models import Reservation

# Create your views here.

@login_required  # Users must be logged in to access this view
def reserve_table(request):
    if request.method == 'POST': # If user is submitting form
        form = ReservationForm(request.POST)
        if form.is_valid():
            Reservation.objects.create(
                user=request.user,  # Link reservation to the logged-in user
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                number_of_guests=form.cleaned_data['number_of_guests'],
                date=form.cleaned_data['date'],
                time=form.cleaned_data['time'],
                special_occasion=form.cleaned_data['special_occasion'],
            )
            return render(request, 'reservations/success.html', {'form' : form})
    else:
        form = ReservationForm() # If user not submitting form then they want a form
    return render(request, 'reservations/reserve_table.html', {'form': form})