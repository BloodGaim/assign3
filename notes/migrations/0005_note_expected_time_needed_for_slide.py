# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20150713_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='expected_time_needed_for_slide',
            field=models.CharField(default=b'0 Minutes', max_length=50),
            preserve_default=True,
        ),
    ]
