#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __date__    : 2019-03-19 20:23
# __author__  : "Zero, by DevOps学院"
# __file__    : dev.py
import os
DEBUG = True
TIME_ZONE = 'Asia/Shanghai'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../adminbackend.db'),
    }
}
