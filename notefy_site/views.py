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
            return HttpResponseRedirect('/')
    else: 
        signup_form = forms.SignupForm()

    return render(request, 'notefy_site/signup.html', {'signup_form': signup_form})
        


