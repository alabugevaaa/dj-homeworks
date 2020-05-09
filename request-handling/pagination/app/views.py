import csv
from urllib.parse import urlencode

from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    all_stations = get_bus_stations()
    paginator = Paginator(all_stations, 10)
    current_page = request.GET.get('page', 1)
    stations = paginator.get_page(current_page)
    prev_page_url, next_page_url = None, None
    if stations.has_previous():
        prev_page_url = urlencode({'page': stations.previous_page_number()})
    if stations.has_next():
        next_page_url = urlencode({'page': stations.next_page_number()})
    return render_to_response('index.html', context={
        'bus_stations': stations,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })


def get_bus_stations():
    with open('data-398-2018-08-30.csv', newline='') as csvfile:
        result = []
        stations = csv.DictReader(csvfile)
        for row in stations:
            station = {'Name': row['Name'],
                       'Street': row['Street'],
                       'District': row['District']}
            result.append(station)
    return result
