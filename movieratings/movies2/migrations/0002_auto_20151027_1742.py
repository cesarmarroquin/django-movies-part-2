# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rater',
            name='gender',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='rater',
            name='occupation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rater',
            name='zip_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='rating',
            name='timestamp',
            field=models.CharField(max_length=200),
        ),
    ]
