# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_client_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('count', models.PositiveSmallIntegerField(default=0)),
                ('comment', models.CharField(max_length=256)),
                ('client', models.ForeignKey(related_name='tasks', to='clients.Client')),
            ],
        ),
    ]
