# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='picture',
            field=models.FileField(null=True, upload_to=b'exercises/images', blank=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='song',
            field=models.FileField(null=True, upload_to=b'exercises/songs', blank=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='type',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='video',
            field=models.FileField(null=True, upload_to=b'exercises/videos', blank=True),
        ),
    ]
