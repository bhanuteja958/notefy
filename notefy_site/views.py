from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    context = {
        'title': 'Notefy - Convert your thoughts to words'
    }
    return render(request, 'notefy_site/home.html', context)

def signup(request):
    if request.method == 'POST':
        signup_form = forms.SignupForm(request.POST)

        if signup_form.is_valid():
            return HttpResponseRedirect('/login')
    else: 
        signup_form = forms.SignupForm()
    
    context = {
        'signup_form': signup_form,
        'title': 'Notefy - Signup'
    }

    return render(request, 'notefy_site/signup.html', context)

def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)

        if login_form.is_valid():
            return HttpResponseRedirect('/')
    else:
        login_form= forms.LoginForm()

    context = {
        'login_form': login_form,
        'title': 'Notefy - Login'
    }

    return render(request, 'notefy_site/login.html', context)

        


