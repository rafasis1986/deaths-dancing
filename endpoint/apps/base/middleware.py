# -*- coding: utf-8 -*-
'''
Created on Sep 6, 2017

@author: rtorres
'''


class HeaderMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
        return response
