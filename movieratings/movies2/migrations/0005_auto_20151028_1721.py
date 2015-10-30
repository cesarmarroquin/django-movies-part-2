# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies2', '0004_auto_20151028_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
