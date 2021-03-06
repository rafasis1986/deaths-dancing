# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_social',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='picture',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='provider',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='provider_id',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
