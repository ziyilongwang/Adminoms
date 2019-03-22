#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __date__    : 2019-03-19 20:23
# __author__  : "Zero, by DevOps学院"
# __file__    : prod.py
import os
DEBUG = True
TIME_ZONE = 'Asia/Shanghai'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../omsBackend.db'),
    }
}

# 开启ldap认证，不开启就注释下面一行
# AUTHENTICATION_BACKENDS = ("django_python3_ldap.auth.LDAPBackend",)
