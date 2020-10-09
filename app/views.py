from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie, Serie, Episode, Genre


MOVIES_DB_NAME = 'movies'


# ROOT
def index(request):
	if request.is_ajax():
		print('\n\n\najax\n\n\n\n')
	return render(request, 'app/movies.html', {})

# MOVIES
def movies_index(request):
	slider_data = Movie.objects.using(MOVIES_DB_NAME).order_by('-id')[:5]
	movies = Movie.objects.using(MOVIES_DB_NAME).order_by('-id')[:20]
	series = Serie.objects.using(MOVIES_DB_NAME).order_by('-id')[:20]
	return render(request, 'app/home.html', {'movies': movies, 'series': series, 'slider_data': slider_data})


def movies(request):
	return render(request, 'app/movies.html', {})


def series(request):
	return render(request, 'app/series.html', {})