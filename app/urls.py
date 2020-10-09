from django.urls import path
from app import views

urlpatterns = [
	# ROOT
	path('', views.index, name='app-index'),
	# MOVIES
	path('movies-app/', views.movies_index, name='app-movies-index'),
	path('movies-app/movies/', views.movies, name='app-movies-movies'),
	path('movies-app/series/', views.series, name='app-movies-series'),
]