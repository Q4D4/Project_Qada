from rest_framework import generics, filters
# Custom Filter
from movies.api_filter import CustomFilterBackend
# Custom Pagination
from movies.api_pagination import CustomListPagination
# Models
from movies.models import Genre, Movie, Serie, Episode
# Serialziers
from movies.serializers import GenreSerializer, MovieListSerializer, MovieDetailSerializer, SerieSerializer, EpisodeSerializer
#scraping
import requests
from bs4 import BeautifulSoup
from multiprocessing import Process
from django.http import HttpResponse
from time import sleep

def scrap(request):
    return HttpResponse('index')


class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all().using('movies')
    serializer_class = GenreSerializer


class GenreDetailView(generics.RetrieveAPIView):
    queryset = Genre.objects.all().using('movies')
    serializer_class = GenreSerializer


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.order_by('-id').using('movies')
    serializer_class = MovieListSerializer
    pagination_class = CustomListPagination
    filter_backends = [filters.OrderingFilter, CustomFilterBackend]
    ordering_fields = ['id', 'year', 'imdb_rating']


class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.order_by('-id').using('movies')
    serializer_class = MovieDetailSerializer


class SerieListView(generics.ListAPIView):
    queryset = Serie.objects.order_by('-id').using('movies')
    serializer_class = SerieSerializer
    pagination_class = CustomListPagination
    filter_backends = [filters.OrderingFilter, CustomFilterBackend]
    ordering_fields = ['id', 'year', 'imdb_rating']


class SerieDetailView(generics.RetrieveAPIView):
    queryset = Serie.objects.order_by('-id').using('movies')
    serializer_class = SerieSerializer
