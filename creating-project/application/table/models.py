from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя столбца')
    width = models.IntegerField(default=1, verbose_name='Ширина столбца')
    ordinal = models.IntegerField(default=0, verbose_name='Порядковый номер')

    class Meta:
        verbose_name = 'Поле таблицы'
        verbose_name_plural = 'Поля таблицы'
        ordering = ['ordinal']

    def __str__(self):
        return f'{self.name}'


class Path(models.Model):
    path = models.CharField(max_length=250, verbose_name='Путь к файлу')

    class Meta:
        verbose_name = 'Путь к файлу'
        verbose_name_plural = 'Пути к файлу'

    def __str__(self):
        return f'{self.path}'

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        self.save()

