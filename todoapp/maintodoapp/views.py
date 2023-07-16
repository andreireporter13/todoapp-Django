#
#
#
from django.shortcuts import render
from .models import Tasks


def home(request):
    tasks = Tasks.objects.all()
    return render(request, 'maintodoapp/home.html', {'tasks': tasks})


def about(request):
    return render(request, 'maintodoapp/about.html')
