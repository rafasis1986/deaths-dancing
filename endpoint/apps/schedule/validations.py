# -*- coding: utf-8 -*-
'''
Created on Sep 10, 2017

@author: rtorres
'''
from filters.schema import base_query_params_schema
from filters.validations import DatetimeWithTZ

bookings_query_schema = base_query_params_schema.extend(
    {
        'date_lt': DatetimeWithTZ(),
        'date_gt': DatetimeWithTZ(),
    })

hours_query_schema = base_query_params_schema.extend(
    {
        'date': DatetimeWithTZ()
    })
