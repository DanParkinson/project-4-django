from django.urls import path
from . import views
from .views import home_reservation_view

urlpatterns = [
    path('', views.homepage, name='home'),  # Home page
    path('reservations/', views.make_reservation, name='make_reservation'),  # Reservation page
    path('next-reservation/', home_reservation_view, name='next_reservation'),  # Next reservation on homepage
]