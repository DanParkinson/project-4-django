from django.urls import path
from .views import account_details
from .views import account_update
from .views import password_update

urlpatterns = [
    path('', account_details, name='account'),
    path('update/', account_update, name='account_update'),
    path('password-update/', password_update, name='password_update'),
]