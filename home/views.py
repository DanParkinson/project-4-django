from django.shortcuts import render # render handles HttpResponse
from reservations.forms import ReservationForm


def homepage(request):
    return render(request, 'home/index.html')

def make_reservation(request):
    form = ReservationForm()  # Create an instance of the form
    return render(request, 'reservations/reserve_table.html', {'form' : form})
    