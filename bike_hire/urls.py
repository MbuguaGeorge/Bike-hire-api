from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registration, name = 'register'),
]