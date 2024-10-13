from django.shortcuts import render
from .forms import ReservationForm # Imports form for reservation

# Create your views here.

def reserve_table(request):
    if request.method == 'POST': # If user is submitting form
        form = ReservationForm(request.POST)
        if form.is_valid():
            # needs stuff for saving to the database
            return render(request, 'reservations/success.html', {'form' : form})
    else:
        form = ReservationForm() # If user not submitting form then they want a form
    return render(request, 'reservations/reserve_table.html', {'form': form})