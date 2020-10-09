from rest_framework import serializers
# Models
from movies.models import Genre, Movie, Serie, Episode

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Movie
        fields = [
            'id',
            'geo_title',
            'en_title',
            'year',
            'imdb_rating',
            'background_image',
            'description',
            'film_poster_low',
            'film_poster_high',
            'genres'
        ]

class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)


    class Meta:
        model = Movie
        fields = [
            'id',
            'geo_title',
            'en_title',
            'year',
            'imdb_rating',
            'background_image',
            'description',
            'film_link_low',
            'film_link_high',
            'film_poster_low',
            'film_poster_high',
            'genres'
        ]


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'



class SerieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Serie
        fields = [
            'id',
            'geo_title',
            'en_title',
            'year',
            'imdb_rating',
            'background_image',
            'description',
            'serie_poster_low',
            'serie_poster_high',
            'genres',
        ]
