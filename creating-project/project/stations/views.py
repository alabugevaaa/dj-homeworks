import os

from django.shortcuts import render
from .models import Route, Station
from django.db.models import Avg, F, FloatField


API_KEY = os.getenv('API_KEY')


def get_stations(request):
    template = 'stations.html'

    routes = Route.objects.all()
    context = {'routes': routes}

    route = Route.objects.get(name=request.GET.get('route'))
    if route:
        stations = Station.objects.filter(routes=route)
        center = stations.aggregate(x=Avg(F('longitude'), output_field=FloatField()),
                                        y=Avg(F('latitude'), output_field=FloatField()))
        context['stations'] = stations
        context['center'] = center
        context['route'] = route
        context['api_key'] = API_KEY
    return render(request, template, context)
