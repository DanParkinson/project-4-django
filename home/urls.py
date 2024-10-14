from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),  # Home page
    path('reservations/', views.make_reservation, name='make_reservation'),  # Reservation page
    path('about-us/', views.about_us, name='about_us'),  # About Us page
    path('menu/', views.menu, name='menu'),  # Menu page
]