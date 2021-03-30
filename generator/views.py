from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    """We render here home.html from templates"""
    return render(request, 'generator/home.html')

def about(request):
    """We render about.html"""
    return render(request, 'generator/about.html')


def password(request):
    """We generate new password and render password.html from templates"""
    the_password = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')

    """To get value from user input we use request"""
    if request.GET.get('uppercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_'))
    """The type returned from request is string"""
    length = int(request.GET.get('length', 12))  # 12 is default value

    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})
