# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.hashers import make_password

ADMIN_EMAIL = 'admin@admin.com'
ADMIN_PASSWORD = 'admin'


def new_admin_user(apps, schema_editor):
    _Client = apps.get_model('base', 'Client')

    _new_admin = _Client(
        username=ADMIN_EMAIL,
        email=ADMIN_EMAIL,
        first_name='admin',
        last_name='user',
        is_active=True,
        is_superuser=True,
        is_staff=True)
    _new_admin.password = make_password(ADMIN_PASSWORD)
    _new_admin.save()


def revert_admin_user(apps, schema_editor):
    _Client = apps.get_model('base', 'Client')
    _Client.objects.get(username=ADMIN_EMAIL).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_set_client_email_unique'),
    ]

    operations = [
        migrations.RunPython(new_admin_user, revert_admin_user)
    ]
