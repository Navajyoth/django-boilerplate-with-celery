# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='photo',
            field=models.FileField(null=True, upload_to=b'images/trainers', blank=True),
        ),
    ]
