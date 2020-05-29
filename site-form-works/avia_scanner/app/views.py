import time
import random

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    cities = cache.get('cities')
    if not cities:
        cities = []
        for city in City.objects.all():
            cities.append(city.name)
        cache.set('cities', cities, 3600)

    term = request.GET.get('term')
    results = [s for s in cities if term in s]
    return JsonResponse(results, safe=False)
