import imp
from django import views
from django.urls import path
from . import views

urlpatterns =[
    path('signup', views.signup, name="signup"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('notes', views.notes, name="notes"),
    path('note-editor/<int:pk>', views.note_editor, name="note_editor"),
    path('add-note', views.add_note, name="add_note"),
    path('', views.home, name='home')
]