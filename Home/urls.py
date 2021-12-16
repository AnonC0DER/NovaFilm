from django.urls import path
from .views import *

# all this urls include in main urls.py file
urlpatterns = [
    path('', HomePage, name='Home'),
    path('movie/<str:pk>/', SingleMoviePage, name='single-movie'),
    path('serial/<str:pk>/', SingleSerialPage, name='single-serial'),
    path('genre/<str:pk>/', SingleGenrePage, name='single-genre'),
    path('director/<str:pk>/', SingleDirectorPage, name='single-director'),
]