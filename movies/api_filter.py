from rest_framework import filters
# Complex Query Filtering
from django.db.models import Q

class CustomFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # Query Params
        title = request.query_params.get('title', None)
        year_min = request.query_params.get('year_min', None)
        year_max = request.query_params.get('year_max', None)
        imdb_min = request.query_params.get('imdb_min', None)
        imdb_max = request.query_params.get('imdb_max', None)
        genre = request.query_params.getlist('genre', None)
        # Filter By Name
        if title is not None:
            try:
                queryset = queryset.filter(Q(geo_title__icontains=title) | Q(en_title__icontains=title))
            except:
                pass
        # Filter By Year
        if year_min is not None and year_max is None:
            try:
                queryset = queryset.filter(year__gte=year_min)
            except:
                pass
        elif year_min is None and year_max is not None:
            try:
                queryset = queryset.filter(year__lte=year_max)
            except:
                pass
        elif year_min is not None and year_max is not None:
            try:
                queryset = queryset.filter(Q(year__gte=year_min), Q(year__lte=year_max))
            except:
                pass
        # Filter By IMDB Rating
        if imdb_min is not None and imdb_max is None:
            try:
                queryset = queryset.filter(imdb_rating__gte=imdb_min)
            except:
                pass
        elif imdb_min is None and imdb_max is not None:
            try:
                queryset = queryset.filter(imdb_rating__lte=imdb_max)
            except:
                pass
        elif imdb_min is not None and imdb_max is not None:
            try:
                queryset = queryset.filter(Q(imdb_rating__gte=imdb_min), Q(imdb_rating__lte=imdb_max))
            except:
                pass
        # Filter By Genre/Genres
        if len(genre) != 0 and genre is not None:
            try:
                queryset = queryset.filter(genres__genre_name__in=genre)
            except:
                pass

        return queryset
