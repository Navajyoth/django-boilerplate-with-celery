# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0003_auto_20150416_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='month_rate_12',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='month_rate_3',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='month_rate_6',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='monthly_rate',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
    ]
