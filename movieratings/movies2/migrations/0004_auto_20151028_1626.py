# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies2', '0003_auto_20151028_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='movieid',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
