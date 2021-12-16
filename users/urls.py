from django.urls import path
from .views import *

urlpatterns = [
    path('', UserProfile, name='profile'),
    path('register/', registerUser, name='register'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
]