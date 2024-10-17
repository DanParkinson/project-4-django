from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from reservations.models import Reservation


@login_required # Users must be logged on to access this view
def account_details(request):
    return render(request, 'account/account_details.html')


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'email']


@ login_required
def account_update(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your details have been updated.")
            return redirect('account')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request,  'account/account_update.html', {'form': form})


@ login_required
def password_update(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
           user = form.save()
           update_session_auth_hash(request, form.user)  # Important to keep the user logged in
           messages.success(request, "Password changed successfully!")
           return redirect('account')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,  'account/password_update.html', {'form': form})

@login_required
def account_delete(request):
    user = request.user
    if request.method == 'POST':
        # delete reservations of the user
        Reservation.object.filter(user=user).delete()
        # delete account
        user.delete()
        
        messages.success(request, "Your account and reservations have been deleted successfully.")
        return redirect('home')
    return render(request, 'account/account_delete.html')

