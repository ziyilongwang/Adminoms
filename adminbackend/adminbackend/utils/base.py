#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __date__    : 2019-03-21 14:55
# __author__  : "Zero, by DevOps学院"
# __file__    : base.py
__author__ = 'zero'
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
from django.core.exceptions import ObjectDoesNotExist
from django_extensions.db.fields import (CreationDateTimeField, ModificationDateTimeField)
from django.db import models
from rest_framework import (serializers, status)
from rest_framework.response import Response
import logging
import traceback
from rest_framework.views import APIView
from functools import wraps

# from web.config import *
logger = logging.getLogger('info')
error_logger = logging.getLogger('error')
info_logger = logging.getLogger('info')


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = CreationDateTimeField('created_at', db_index=True)
    updated_at = ModificationDateTimeField('updated_at', db_index=True)

    def save(self, **kwargs):
        self.update_updated_at = kwargs.pop('update_updated_at', getattr(self, 'update_updated_at', True))
        super(BaseModel, self).save(**kwargs)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            print (key,value)
        self.save()


    '''
      创建数据和更新数据使用create方法
    '''

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        obj.save()
        return obj

    '''
    '''

    def __str__(self):
        return '{} <{}>'.format(self.__class__.__name__, self.id)

    def __repr__(self):
        return '{} <{}>'.format(self.__class__.__name__, self.id)

    '''
    通过id返回obeject
    '''

    @classmethod
    def get_object_by_pk(cls, pk):
        return cls.objects.get(pk=pk)

    '''
    查询所有数据
    '''

    @classmethod
    def fetch(cls, **kwargs):
        return cls.objects.filter(**kwargs)

    '''
    查询单条数据
    '''

    @classmethod
    def fetch_one(self, **kwargs):
        try:
            res = self.objects.get(**kwargs)
            return res
        except self.DoesNotExist:
            print("DoesNotExist")
            return None
        except Exception as ex:
            raise

    @classmethod
    def pagination(cls, page=1, per_page=10, **kwargs):
        query_set = cls.fetch(**kwargs)
        paginator = Paginator(query_set, per_page)
        try:
            page = paginator.validate_number(page)
        except PageNotAnInteger:
            page = 1
        except EmptyPage:
            return [], paginator.count
        return paginator.get_page(page), paginator.count

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)
        abstract = True


class BaseAPIView(APIView):
    record = None

    @classmethod
    def pagination(cls, data, total, page=1, per_page=10):
        headers = {
            'page': page,
            'per_page': per_page,
            'total': total
        }
        return Response(data, headers=headers)

    @classmethod
    def check_record(cls, model):
        def decorate(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                pk = kwargs.get('pk')
                print(model)
                try:
                    record = model.get_object_by_pk(pk)
                except ObjectDoesNotExist as e:
                    return Response({}, status=status.HTTP_404_NOT_FOUND)
                else:
                    cls.record = record
                return func(*args, **kwargs)

            return wrapper

        return decorate


class BasePaginationSerializer(serializers.Serializer):
    page = serializers.IntegerField(default=1)
    per_page = serializers.IntegerField(default=10)
