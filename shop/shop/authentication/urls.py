from django.urls import path, include
from .views import *



urlpatterns = [
    path('login', loginPage, name='login'),
    path('register', registerPage, name='register'),
    path('me', me, name='me'),
    path('logout', doLogout, name='logout'),


    
]

