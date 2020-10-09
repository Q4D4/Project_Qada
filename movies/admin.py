from django.contrib import admin
# Models
from movies.models import Genre, Movie, Serie, Episode

# Database Config For Movies
class MultiDBModelAdminMovies(admin.ModelAdmin):
    using = 'movies'

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

# Register Models
admin.site.register(Genre, MultiDBModelAdminMovies)
admin.site.register(Movie, MultiDBModelAdminMovies)
admin.site.register(Serie, MultiDBModelAdminMovies)
admin.site.register(Episode, MultiDBModelAdminMovies)
