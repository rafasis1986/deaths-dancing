# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 14:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_ordering_bookings'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=set([('date', 'hour')]),
        ),
    ]