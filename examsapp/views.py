# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import CurrentAffair

def home(request):
    return render(request, 'index.html')

def current_affairs(request):
    current_affairs = CurrentAffair.objects.all()
    return render(request, 'current_affairs.html', {'current_affairs': current_affairs})

def sql_practice(request):
    sql_practice = CurrentAffair.objects.all()
    return render(request, 'sql_practice.html', {'sql_practice': sql_practice})

def login(request):
    # login = CurrentAffair.objects.all()
    return render(request, 'login.html', {'login': login})