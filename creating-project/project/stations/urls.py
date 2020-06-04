from django.urls import path

from .views import get_stations

urlpatterns = [
    path('stations/', get_stations, name='stations'),
]