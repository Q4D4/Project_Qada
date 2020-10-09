from django.db import models

class Genre(models.Model):
    genre_name          = models.CharField(max_length=100, unique=True)


    class Meta:
        db_table        = 'genre'


    def __str__(self):
        return self.genre_name


class Movie(models.Model):
    geo_title           = models.CharField(max_length=200, null=True, blank=True)
    en_title            = models.CharField(max_length=200, null=True, blank=True)
    year                = models.IntegerField(null=True, blank=True)
    imdb_rating         = models.FloatField(null=True, blank=True)
    background_image    = models.CharField(max_length=10000, null=True, blank=True)
    description         = models.TextField(max_length=100000, null=True, blank=True)
    film_link_low       = models.CharField(max_length=100000)
    film_link_high      = models.CharField(max_length=100000)
    film_poster_low     = models.CharField(max_length=100000)
    film_poster_high    = models.CharField(max_length=100000)
    genres              = models.ManyToManyField(Genre, blank=True)


    class Meta:
        db_table        = 'movie'


    def __str__(self):
        response        = str(self.geo_title) + ' | ' + str(self.en_title)
        return response


class Serie(models.Model):
    geo_title           = models.CharField(max_length=200, null=True, blank=True)
    en_title            = models.CharField(max_length=200, null=True, blank=True)
    year                = models.IntegerField(null=True, blank=True)
    imdb_rating         = models.FloatField(null=True, blank=True)
    background_image    = models.CharField(max_length=10000, null=True, blank=True)
    description         = models.TextField(max_length=100000, null=True, blank=True)
    serie_poster_low    = models.CharField(max_length=100000)
    serie_poster_high   = models.CharField(max_length=100000)
    genres              = models.ManyToManyField(Genre, blank=True)


    class Meta:
        db_table        = 'serie'


    def __str__(self):
        response        = str(self.geo_title) + ' | ' + str(self.en_title)
        return response


class Episode(models.Model):
    serie               = models.ForeignKey(Serie, on_delete=models.CASCADE)
    season              = models.IntegerField()
    episode             = models.IntegerField()
    episode_link_low    = models.CharField(max_length=100000)
    episode_link_high   = models.CharField(max_length=100000)


    class Meta:
        db_table        = 'episode'


    def __str__(self):
        response        = str(self.serie) + ' | ' + str(self.season) + ' | ' + str(self.episode)
        return response
