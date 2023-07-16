#
#
#
from django.shortcuts import render


def home(request):
    return render(request, 'maintodoapp/home.html')


def about(request):
    return render(request, 'maintodoapp/about.html')
