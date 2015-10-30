# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies2', '0002_auto_20151027_1742'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Actors',
        ),
        migrations.DeleteModel(
            name='Links',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
    ]
