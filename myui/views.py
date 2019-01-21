from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    context = {}
    return render(request, 'events/index.html', context)


def signin(request):
    context = {}
    return render(request, 'users/signin.html', context)


def signup(request):
    context = {}
    return render(request, 'users/signup.html', context)
