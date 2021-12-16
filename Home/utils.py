from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateMovies(request, movies, results):
    page = request.GET.get('page')
    paginator = Paginator(movies, results)

    try:
        movies = paginator.page(page)

    except PageNotAnInteger:
        page = 1
        movies = paginator.page(page)
    
    except EmptyPage:
        page = paginator.num_pages
        movies = paginator.page(page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, movies


def searchMovies_Serials(request):
    # default search query is '' -> all objects
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # filter objects by search query

    movies = HomePageModel.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(summary__icontains=search_query) |
        Q(director__name__icontains=search_query) |
        Q(genre__name__icontains=search_query)
    )

    serials = Serial.objects.distinct().filter(
        Q(Serial_name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(summary__icontains=search_query) |
        Q(director__name__icontains=search_query) |
        Q(genre__name__icontains=search_query)
    )
    
    return movies, search_query, serials