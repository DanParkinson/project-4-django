from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required # Users must be logged on to access this view
def account_details(request):
    return render(request, 'account/account_details.html')