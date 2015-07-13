# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20150713_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='created',
        ),
        migrations.RemoveField(
            model_name='note',
            name='done',
        ),
        migrations.RemoveField(
            model_name='note',
            name='due',
        ),
        migrations.RemoveField(
            model_name='note',
            name='updated',
        ),
        migrations.AddField(
            model_name='presentation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presentation',
            name='done',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presentation',
            name='time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presentation',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
    ]
