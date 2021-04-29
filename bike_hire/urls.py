from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registration, name = 'register'),
    path('userlist', views.userlist.as_view(), name = 'userlist'),
    path('token', views.TokenView.as_view()),
    path('profile', views.profiling, name = 'profile'),
]