from django.urls import path
from . import views

urlpatterns = [
    path('reserve/', views.reserve_table, name='make_reservation'),  # The URL pattern name should be 'make_reservation'
]