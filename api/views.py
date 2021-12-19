from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from Home.models import HomePageModel
from rest_framework import generics


# all routes - only get method 
@api_view(['GET'])
def getRoutes(request):
    '''
    All available api urls
    '''
    routes = [
        {'GET' : 'docs/'},
        {'GET' : 'movies/'},
        {'GET' : 'movie/id/'},
        {'GET' : 'series/'},
        {'GET' : 'serial/id/'},

        {'POST' : 'users/register/'},
        {'POST' : 'users/token/'},
        {'POST' : 'users/token/refresh/'},
    ]

    return Response(routes)



# get all movie objects - only get method 
@api_view(['GET'])
def getMovies(request):
    '''
    <br>
    ### Description for source code
    1. Movies variable is related to HomePageModel to get all movie objects <br>
    2. Serializer variable is related to MoviesSerializer to converting objects into 
    data types understandable by front-end (json, xml) - many=True because there are more than one movie objects <br>
    3. Return serializer.data which is the json data.
    <br>
    '''
    movies = HomePageModel.objects.all()
    serializer = MoviesSerializer(movies, many=True)

    return Response(serializer.data)



# get movie object - only get method 
@api_view(['GET'])
# authenticate to get results
@permission_classes([IsAuthenticated])
def getMovie(request, pk):
    '''
    <br>
    ## You have to use authorization token
    ### Description for source code
    1. Movie is related to HomePageModel to get the movie object by id <br>
    2. Serializer is related to MoviesSerializer to converting objects into 
    data types understandable by front-end (json, xml) - many=False because there's only one movie object <br>
    3. Return serializer.data which is the json data.
    <br>
    <br>
    '''
    movie = HomePageModel.objects.get(id=pk)
    serializer = MoviesSerializer(movie, many=False)

    return Response(serializer.data)



# get series objects - only get method 
@api_view(['GET'])
def getSeries(request):
    '''
    <br>
    ## You have to use authorization token
    ### Description for source code
    1. Series variable is related to Serial Model to get all serial objects <br>
    2. Serializer variable is related to SeriesSerializer to converting objects into 
    data types understandable by front-end (json, xml) - many=True because there are more than one movie objects <br>
    3. return serializer.data which is the json data.
    <br>
    <br>
    '''
    series = Serial.objects.all()
    serializer = SeriesSerializer(series, many=True)

    return Response(serializer.data)



# get series object - only get method 
@api_view(['GET'])
# authenticate to get results
@permission_classes([IsAuthenticated])
def getSerial(request, pk):
    '''
    <br>
    ## You have to use authorization token
    ### Description for source code
    1. Serial is related to Serial Model to get the serial object by id <br>
    2. Serializer variable is related to SeriesSerializer to converting objects into 
    data types understandable by front-end (json, xml) - many=False because there's only one serial object. <br>
    3. return serializer.data which is the json data.
    <br>
    <br>
    '''
    serial = Serial.objects.get(id=pk)
    serializer = SeriesSerializer(serial, many=False)
    
    return Response(serializer.data)



# Register a new user
## We use class-based views to keep out code DRY (Don't repeat yourself), More details : https://www.geeksforgeeks.org/class-based-vs-function-based-views-which-one-is-better-to-use-in-django/#:~:text=The%20most%20significant%20advantage%20of,and%20over%20in%20your%20boilerplate.
class UserCreate(generics.CreateAPIView):
    '''
    <br>
    ### Description for source code
    1. register is related to User Django model, [ref](https://docs.djangoproject.com/en/4.0/ref/contrib/auth/) <br>
    2. serializer_class is related to RegisterSerializer to converting objects into 
    data types understandable by front-end (json, xml) <br>
    3. We can choose which kind of users can access, [More details](https://code.djangoproject.com/ticket/27950) <br>
    <br>
    <br>
    '''
    register = User.objects.all()
    serializer_class = RegisterSerializer
    permission_class = (AllowAny, )


# github.com/AnonC0DER