from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import *
from .models import *
from Home.models import HomePageModel, Serial
from django.contrib.auth.decorators import login_required
import random


# Create your views here.
# Register
def registerUser(request):
    # use this variable in front end
    page = 'register'
    # use register form model
    form = Register()

    # if method is post, get the data
    if request.method == 'POST':
        form = Register(request.POST)
        # check the data
        if form.is_valid():
            # save but don't commit new data
            user = form.save(commit=False)
            # make username lower letter and then save the data
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            # redirect the user to profile page
            login(request, user)
            return redirect('profile')

        else:
            messages.error(
                request, 'An error has occurred during registration')

    # send data to front end
    context = {'page' : page, 'form' : form}
    return render(request, 'users/login_register.html', context)



# Login
def loginUser(request):
    # use this variable in front end
    page = 'login'

    # if user is authenticated redirect the user to profile page
    if request.user.is_authenticated:
        return redirect('profile')

    # if method is post, save username and password
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # try to get username except the user name does not exist
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist !')

        # authenticate the user
        user = authenticate(request, username=username, password=password)

        # if user variable isn't none, login
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'profile')
        
        else:
            messages.error(request, 'Username or password is incorrect !')
        
    return render(request, 'users/login_register.html')



# Logout
def logoutUser(request):
    logout(request)
    messages.success(request, 'Successfully Logged out !')
    return redirect('Home')



# Profile
@login_required(login_url='login')
def UserProfile(request):
    # get user name
    profile = request.user
    # get movies and series, then filter them by created date
    movies = HomePageModel.objects.filter().order_by('-created') 
    series = Serial.objects.filter().order_by('-created')
    # get 10 random movies for random section 
    random_movies = random.sample(list(HomePageModel.objects.all()), 10)
    # profile form
    form = ProfileUser(instance=profile)

    # check the method
    if request.method == 'POST':
        form = ProfileUser(request.POST, instance=profile)
        # if the data is valid save the data
        if form.is_valid():
            form.save()
            return redirect('profile')

    # send context to front end
    context = {'profile' : profile, 'movies' : movies,
     'series' : series, 'rand' : random_movies, 'form' : form}
    return render(request, 'users/profile.html', context)