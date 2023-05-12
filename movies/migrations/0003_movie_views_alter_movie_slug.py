# Generated by Django 4.2.1 on 2023-05-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]