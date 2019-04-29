#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __date__    : 2019-04-02 17:34
# __author__  : "Zero, by DevOps学院"
# __file__    : django.py
# -*- coding: utf-8 -*-
# author: itimor

from django.utils.deprecation import MiddlewareMixin


class DisableCSRF(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
