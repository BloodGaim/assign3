# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_auto_20150815_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presentation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='user',
        ),
    ]
