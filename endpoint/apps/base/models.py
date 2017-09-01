# -*- coding: utf-8 -*-
'''
Created on Sep 1, 2017

@author: rtorres
'''
from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(AbstractUser, models.Model):

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        db_table = 'base_client'

    class JSONAPIMeta:
        resource_name = 'client'
