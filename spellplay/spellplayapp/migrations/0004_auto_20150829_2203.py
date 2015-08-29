# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spellplayapp', '0003_auto_20150829_2140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ['-final_score']},
        ),
        migrations.AlterField(
            model_name='score',
            name='final_score',
            field=models.IntegerField(),
        ),
    ]
