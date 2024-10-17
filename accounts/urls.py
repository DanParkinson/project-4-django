from django.urls import path
from .views import account_details

urlpatterns = [
    path('', account_details, name='account'),
]