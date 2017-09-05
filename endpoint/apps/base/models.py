# -*- coding: utf-8 -*-
'''
Created on Sep 1, 2017

@author: rtorres
'''
from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(AbstractUser, models.Model):
    picture = models.URLField(null=True)
    is_social = models.BooleanField(default=False)
    provider = models.CharField(max_length=30, null=True)
    provider_id = models.CharField(max_length=30, null=True)
    email = models.EmailField(unique=True, db_index=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        db_table = 'base_client'

    class JSONAPIMeta:
        resource_name = 'client'

    @property
    def full_name(self):
        return self.get_full_name()
