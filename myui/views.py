from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def comments(request):
    context = {}
    return render(request, 'comments/index.html', context)


def home(request):
    context = {}
    return render(request, 'events/index.html', context)


def signin(request):
    context = {}
    return render(request, 'users/signin.html', context)


def signup(request):
    context = {}
    return render(request, 'users/signup.html', context)


def create_event(request):
    context = {}
    return render(request, 'events/create.html', context)


def detail_event(request, id_event):
    context = {}
    return render(request, 'events/detail.html', context)
