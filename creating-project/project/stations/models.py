from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=10, verbose_name="Название")

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

    def __str__(self):
        return self.name


class Station(models.Model):
    latitude = models.FloatField(max_length=50, verbose_name="Широта")
    longitude = models.FloatField(max_length=50, verbose_name="Долгота")
    routes = models.ManyToManyField(Route, related_name="stations")
    name = models.CharField(max_length=50, verbose_name="Название")

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'

    def __str__(self):
        return self.name
