# Generated by Django 2.2.10 on 2020-06-04 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(max_length=50, verbose_name='Широта')),
                ('longitude', models.FloatField(max_length=50, verbose_name='Долгота')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('routes', models.ManyToManyField(related_name='stations', to='stations.Route')),
            ],
        ),
    ]
