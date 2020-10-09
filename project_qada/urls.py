from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio-api/', include('portfolio.urls')),
    path('movies-api/', include('movies.urls')),
    path('', include('app.urls')),
]
