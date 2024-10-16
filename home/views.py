from django.shortcuts import render # render handles HttpResponse
from reservations.forms import ReservationForm

# for loading the home reservation view
from django.utils import timezone
from reservations.models import Reservation


def homepage(request):
    return render(request, 'home/index.html')

def make_reservation(request):
    form = ReservationForm()  # Create an instance of the form
    return render(request, 'reservations/reserve_table.html', {'form' : form})

def about_us(request):
    return render(request, 'home/about_us.html')  #"About Us" page

def menu(request):
    return render(request, 'home/menu.html')  #"Menu" page

# loads the logged in users next reservation onto the homepage
def home_reservation_view(request):
    now = timezone.now()

    next_reservation = Reservations.objects.filter(user=request.user,date__gte=now.date()).order_by('date', 'time').first()

    return render(request, 'home.html', {'next_reservation': next_reservation})

    