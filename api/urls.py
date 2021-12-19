from re import I
from django.urls import path
from .views import *
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', getRoutes),
    path('docs/', include_docs_urls(title='NovaFilmAPI-docs')),
    path('movies/', getMovies),
    path('movie/<str:pk>/', getMovie),
    path('series/', getSeries),
    path('serial/<str:pk>/', getSerial),

    path('users/register/', UserCreate.as_view()),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
    path('schema/', get_schema_view(
        title='NovaFilmAPI-schema',
        description='NovaFilmAPI-schema',
        version='1.0.0'
    ), name='openapi-schema'),
]