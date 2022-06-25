from django.shortcuts import redirect, render
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def home(request):
    context = {
        'title': 'Notefy - Convert your thoughts to words'
    }
    return render(request, 'notefy_site/home.html', context)

def signup(request):
    if request.method == 'POST':
        signup_form = forms.SignupForm(request.POST)

        if signup_form.is_valid():
            if signup_form.cleaned_data['password'] != signup_form.cleaned_data['confirm_password']:
                messages.error(request, 'Password and Confirm Password should be same', extra_tags='password_error')
            elif (User.objects.filter(username=signup_form.cleaned_data['user_name']).exists()):
                messages.info(request, 'Username already taken')
            elif(User.objects.filter(email=signup_form.cleaned_data['email']).exists()):
                messages.info(request, 'Email already taken')
            else:
                new_user = User(
                    username=signup_form.cleaned_data['user_name'],
                    email=signup_form.cleaned_data['email'],
                    password=make_password(signup_form.cleaned_data['password'])
                )
                new_user.save()
                return HttpResponseRedirect('/login')
    else: 
        signup_form = forms.SignupForm()
    
    context = {
        'signup_form': signup_form,
        'title': 'Notefy - Signup'
    }

    return render(request, 'notefy_site/signup.html', context)

def login_user(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)

        if login_form.is_valid():
            user = User.objects.get(email=login_form.cleaned_data['email'])
            if user:
                username = user.username
                user = authenticate(username=username, password=login_form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else: 
                    messages.error('Please enter correct email/passowrd')
                    
            else:
                messages.error('Please enter correct email/passowrd')

            return HttpResponseRedirect('/')
    else:
        login_form= forms.LoginForm()

    context = {
        'login_form': login_form,
        'title': 'Notefy - Login'
    }

    return render(request, 'notefy_site/login.html', context)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def notes(request):
    context = {
        'title': 'Notefy - Notes'
    }
    return render(request, 'notefy_site/notes.html', context)

def add_note(request):
    current_user = request.user
    newNote = models.Note(title='Example Title', content='Example Content', created_by=current_user)
    newNote.save()
    return redirect(f'/note-editor/{newNote.pk}')

def note_editor(request, pk):
    note = models.Note.objects.get(id=pk)

    if note:
        if request.method == 'POST':
            note_form = forms.NoteForm(request.POST)
            if note_form.is_valid():
                title = note_form.cleaned_data['title']
                markdown = note_form.cleaned_data['markdown']
                note.title = title
                note.content = markdown
                note.save()
                return redirect(f'/note-editor/{pk}')
        else:
            form_data = {
                'title': note.title,
                'markdown': note.content
            }
            note_form = forms.NoteForm(data=form_data)
    else:
        return redirect('/notes')

    context = {
        'title': 'Notefy - Editor',
        'note_form': note_form,
        'note': note
    }
    return render(request, 'notefy_site/note_editor.html', context)


        


