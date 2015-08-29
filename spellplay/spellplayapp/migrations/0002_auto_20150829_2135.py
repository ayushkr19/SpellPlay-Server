# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spellplayapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ['-total_words']},
        ),
        migrations.AddField(
            model_name='score',
            name='final_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
