# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20150712_1436'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Folder',
            new_name='Presentation',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='folder',
            new_name='presentation',
        ),
    ]
