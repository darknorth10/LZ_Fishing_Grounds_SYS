from django.shortcuts import render
from ..users.forms import SignInForm
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')