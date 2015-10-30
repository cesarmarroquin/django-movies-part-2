# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('movie_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('character_name', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('imdbid', models.IntegerField(default=0)),
                ('tmdbid', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('gender', models.CharField(max_length=7, default='male')),
                ('age', models.IntegerField(default=0)),
                ('occupation', models.CharField(max_length=200)),
                ('zip_code', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('rating', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(to='movies2.Movie')),
                ('rater', models.ForeignKey(to='movies2.Rater')),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('movieid', models.CharField(max_length=50)),
                ('rating', models.FloatField(default=0)),
                ('timestamp', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('tag', models.CharField(max_length=200)),
                ('timestamp', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('movieid', models.ForeignKey(to='movies2.Movie')),
            ],
        ),
    ]
