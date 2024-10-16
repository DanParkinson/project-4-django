from django.urls import path
from . import views

urlpatterns = [
    path('reserve/', views.reserve_table, name='make_reservation'),  # The URL pattern name should be 'make_reservation'
    path('my-reservations/', views.my_reservations, name='my_reservations'), # Path for viewing user's reservations
    path('edit/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),  # Edit reservation
]