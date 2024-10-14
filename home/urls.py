from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),  # Home page
    path('reservations/', views.make_reservation, name='make_reservation'),  # Reservation page
]