from django.shortcuts import render

from users.models import User
from users.forms import UserLoginForm


def login(request):
    contex = {'form': UserLoginForm()}
    return render(request, 'users/login.html', contex)


def registration(request):
    return render(request, 'users/registration.html')

