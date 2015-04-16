# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='excercise',
            field=models.ForeignKey(related_name='tasks', default=0, to='exercises.Exercise'),
            preserve_default=False,
        ),
    ]
