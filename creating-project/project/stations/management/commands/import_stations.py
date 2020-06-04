import csv

from django.core.management import BaseCommand
from stations.models import Route, Station


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('moscow_bus_stations.csv', 'r') as csvfile:

            station_reader = csv.reader(csvfile, delimiter=';')
            next(station_reader)

            for line in station_reader:
                latitude = line[3]
                longitude = line[2]
                routes = line[7]
                routes = routes.split('; ')
                name = line[1]
                station = Station.objects.create(latitude=latitude, longitude=longitude, name=name)
                for route in routes:
                    route, created = Route.objects.get_or_create(name=route)
                    route.stations.add(station)



