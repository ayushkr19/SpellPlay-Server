# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spellplayapp', '0002_auto_20150829_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='final_score',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
