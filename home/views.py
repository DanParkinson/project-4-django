from django.shortcuts import render # render handles HttpResponse
from reservations.forms import ReservationForm


def homepage(request):
    return render(request, 'home/index.html')

def make_reservation(request):
    form = ReservationForm()  # Create an instance of the form
    return render(request, 'reservations/reserve_table.html', {'form' : form})

def about_us(request):
    return render(request, 'home/about_us.html')  # New "About Us" page

def menu(request):
    return render(request, 'home/menu.html')  # New "Menu" page
    