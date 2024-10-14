from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'), # home page
     path('reservations/', views.make_reservation, name='make_reservation'),  # Reservation page
]