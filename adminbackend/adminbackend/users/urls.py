#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __date__    : 2019-03-22 09:44
# __author__  : "Zero, by DevOps学院"
# __file__    : urls.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from users.views import UserViewSet, RoleViewSet, GroupViewSet

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'roles', RoleViewSet)
