import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from phones.models import Phone
from decimal import Decimal
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                price = Decimal(line[3].replace(',', '.'))
                release_date = datetime.strptime(line[4], '%Y-%m-%d')
                Phone.objects.create(id=line[0], name=line[1], price=price, image=line[2],
                                     release_date=release_date, lte_exists=line[5], slug=slugify(line[1]))
