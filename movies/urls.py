from django.urls import path
from movies import views

urlpatterns = [
    path('', views.scrap),
    path('genres/', views.GenreListView.as_view(), name='movies-genre-list'),
    path('genres/<int:pk>', views.GenreDetailView.as_view(), name='movies-genre-detail'),
    path('movies/', views.MovieListView.as_view(), name='movies-movie-list'),
    path('movies/<int:pk>', views.MovieDetailView.as_view(), name='movies-movie-detail'),
    path('series/', views.SerieListView.as_view(), name='movies-serie-list'),
    path('series/<int:pk>', views.SerieDetailView.as_view(), name='movies-serie-detail'),
]
