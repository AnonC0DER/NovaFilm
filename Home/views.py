from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .utils import *
from .forms import *

# Create your views here.
def HomePage(request):
    # Filter movies by search query
    Movies, search_query, serials = searchMovies_Serials(request)
    # Manage pagination bar
    custom_range, Movies = paginateMovies(request, Movies, 9) # 9 post per page
    # get all genres for navbar
    Navbar_genre = Genre.objects.all()
    # get the most popular movies
    Most_views_movies = HomePageModel.objects.all().order_by('-page_view') 
    # get all serials
    Serials_new = Serial.objects.all()

    # send data
    context = {
        'movies' : Movies, 'serials' : serials, 'popular' : Most_views_movies,
    'genres' : Navbar_genre, 'search_query' : search_query,
     'custom_range' : custom_range, 'new_serials' : Serials_new
     }
    return render(request, 'Home/home.html', context)



# Single Serial Page
def SingleSerialPage(request, pk):
    # get serial object by id
    serial = Serial.objects.get(id=pk)
    # comments
    forms = CommentsFormSerial()
    if request.method == 'POST':
        form = CommentsFormSerial(request.POST)
        review = form.save(commit=False)
        review.serial_page = serial
        review.save()
        
        return redirect('single-serial', pk=serial.id)


    # count page view
    serial.page_view = serial.page_view + 1
    # get all movies for "New Movies"
    Movies = HomePageModel.objects.all()
    # get similar serials for "Similar Serials" section in front-end
    Similar_Serials = Serial.objects.all().distinct().filter(genre__in=serial.genre.all())
    # get all genres for navbar
    Navbar_genre = Genre.objects.all()
    # get all comments
    comments_all = serial.comments_serial.all()

    context = {
        'serial' : serial, 'similar' : Similar_Serials,
        'view' : serial.page_view, 'genres' : Navbar_genre,
        'movies' : Movies, 'comments_all' : comments_all, 'forms' : forms
    }
    return render(request, 'Home/single-serial.html', context)



# Single Movie Page
def SingleMoviePage(request, pk):
    # get movie object by id
    Movie = HomePageModel.objects.get(id=pk)
    # comments
    forms = CommentsForm()
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        review = form.save(commit=False)
        review.movie_page = Movie
        review.save()

        return redirect('single-movie', pk=Movie.id)

    # count page view
    Movie.page_view = Movie.page_view + 1
    # get all movies for "New items" section in front-end 
    Movies = HomePageModel.objects.all()
    # get similar movies for "Similar Movies" section in front-end
    Similar_Movies = HomePageModel.objects.all().filter(genre__in=Movie.genre.all()).distinct()
    # get all genres for navbar
    Navbar_genre = Genre.objects.all()
    # get all serials
    Serials = Serial.objects.all()
    # get all comments
    comments_all = Movie.comments.all()

    # send all data
    context = {'movie' : Movie, 'movies' : Movies, 'similar' : Similar_Movies,
    'view' : Movie.page_view, 'genres' : Navbar_genre, 'serials' : Serials,
     'forms' : forms, 'comments_all' : comments_all}
    return render(request, 'Home/single-movie.html', context)



# Single Genre Page
def SingleGenrePage(request, pk):
    # get genre object by id
    genre = Genre.objects.get(id=pk)
    # get movies by genre
    Movies_filtered = HomePageModel.objects.all().filter(genre=genre).distinct()
    # get serial by genre
    Serials_filtered = Serial.objects.all().filter(genre=genre).distinct()
    # Serial_Movies_filtered = HomePageModel.objects.all().filter(genre=genre).distinct(), Serial.objects.all().filter(genre=genre).distinct()
    # get all movies
    Movies = HomePageModel.objects.all()
    # get all genres for navbar
    Navbar_genre = Genre.objects.all()
    # get all serials
    Serials = Serial.objects.all()

    context = {'genre' : genre, 'movies_filtered' : Movies_filtered,
     'serials_filtered' : Serials_filtered, 'movies' : Movies, 
     'genres' : Navbar_genre, 'serials' : Serials}
    return render(request, 'Home/single-genre.html', context)
    


# Director
def SingleDirectorPage(request, pk):
    # director by id
    director = Director.objects.get(id=pk)
    # filter movies by director id
    Movies_filtered = HomePageModel.objects.all().filter(director=director).distinct()
    # get serial by genre
    Serials_filtered = Serial.objects.all().filter(director=director).distinct()
    # get all movies
    Movies = HomePageModel.objects.all()
    # get all genres for navbar
    Navbar_genre = Genre.objects.all()
    # get all serials
    Serials = Serial.objects.all()

    context = {'director' : director, 'movies_filtered' : Movies_filtered,
    'serials_filtered' : Serials_filtered, 'movies' : Movies, 
    'genres' : Navbar_genre, 'serials' : Serials}
    return render(request, 'Home/single-director.html', context)