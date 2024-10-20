from django.shortcuts import render # render handles HttpResponse
from reservations.forms import ReservationForm
# for loading the homepage view
from django.utils import timezone
from reservations.models import Reservation
from django.contrib.auth.decorators import login_required # users must log in to reserve


def homepage(request):
    now = timezone.now()
    next_reservation = None # for not logged in users

    # for displaying the logged in users next reservation
    if request.user.is_authenticated: # check if logged in
        next_reservation = Reservation.objects.filter(
            user=request.user, # get user id
            date__gte=now.date(), # filter date as today onwards. removes expired reservations
            time__gte=now.time(), # filter time as current time onwards. removes expired reservations
        ).order_by('date').first() # order by date and show the first one 

    return render(request, 'home/index.html', {'next_reservation': next_reservation})

def make_reservation(request):
    form = ReservationForm()  # Create an instance of the form
    return render(request, 'reservations/reserve_table.html', {'form' : form})

def about_us(request):
    return render(request, 'home/about_us.html')  #"About Us" page

def menu(request):
    return render(request, 'home/menu.html')  #"Menu" page


    