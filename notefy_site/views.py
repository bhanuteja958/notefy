from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'title': 'Notefy - Convert your thoughts to words'
    }
    return render(request, 'notefy_site/home.html', context)

