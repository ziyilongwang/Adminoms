#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __date__    : 2019-03-19 20:22
# __author__  : "Zero, by DevOps学院"
# __file__    : __init__.py.py

# -*- coding: utf-8 -*-


import platform
# 判断机器的名字是否是10.10.10.1，如果是的话就加载正式环境的配置，否则就认为是开发环境
if platform.node() == "10.10.10.1":
    print("正式环境")
    from adminbackend.settings.base import *
    from adminbackend.settings.prod import *
else:
    print("开发环境")
    from adminbackend.settings.base import *
    from adminbackend.settings.dev import *
