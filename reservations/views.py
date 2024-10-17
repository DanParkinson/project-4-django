from django.contrib.auth.decorators import login_required # users must log in to reserve
from django.shortcuts import render
from .forms import ReservationForm # Imports form for reservation
from .models import Reservation
from django.shortcuts import get_object_or_404, redirect # for editing reservations
from django.utils import timezone # for displaying my_reservations in time order

# Create your views here.

# Users to be able to reserve a table
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

@login_required  # Users must be logged in to access this view
def my_reservations(request):
    now = timezone.now()  # Get the current date and time
    # Retrieve the user's reservations ordered by date and time (closest first)
    # Filters out expired reservations
    user_reservations = Reservation.objects.filter(
        user=request.user, # get user id
        date__gte=now.date(), # filter date as today onwards. removes expired reservations
        time__gte=now.time(), # filter time as current time onwards. removes expired reservations
        ).order_by('date') # order by date

    return render(request, 'reservations/my_reservations.html', {'reservations': user_reservations})


# Users can edit their reservations
@login_required  # Users must be logged in to access this view
def edit_reservation(request, reservation_id):
    user_reservation = get_object_or_404(Reservation, id = reservation_id, user = request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=user_reservation)
        if form.is_valid():
            form.save()  # Save the updated reservation
            return redirect('my_reservations')  # Redirect to my reservations page
    else:
        form = ReservationForm(instance=user_reservation)  # Pre-fill the form with existing data

    return render(request, 'reservations/edit_reservation.html', {'form': form})

# users can delete their reservations
@login_required  # Users must be logged in to access this view
def delete_reservation(request, reservation_id):
    user_reservation = get_object_or_404(Reservation, id = reservation_id, user = request.user)
    if request.method == 'POST':  # Deleting only on POST request
        user_reservation.delete()
        return redirect('my_reservations')  # Redirect back to the user's reservations after deletion
        
    return render(request, 'reservations/confirm_delete.html', {'reservation': user_reservation})

