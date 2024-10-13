from django.shortcuts import render # render handles HttpResponse

def homepage(request):
    return render(request, 'home/index.html')
    