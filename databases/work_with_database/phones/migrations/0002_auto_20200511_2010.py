# Generated by Django 2.2.10 on 2020-05-11 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='release_data',
            new_name='release_date',
        ),
    ]