# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='rate',
        ),
        migrations.AddField(
            model_name='trainer',
            name='month_rate_12',
            field=models.PositiveSmallIntegerField(default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='month_rate_3',
            field=models.PositiveSmallIntegerField(default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='month_rate_6',
            field=models.PositiveSmallIntegerField(default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='monthly_rate',
            field=models.PositiveSmallIntegerField(default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trainer',
            name='photo',
            field=models.FileField(upload_to=b'images/trainers', blank=True),
        ),
    ]
