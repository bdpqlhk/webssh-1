#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class HostTmp(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    unique = models.CharField(max_length=40, unique=True)
    host = models.CharField(max_length=32)
    port = models.IntegerField()
    user = models.CharField(max_length=32)
    auth = models.CharField(max_length=16)
    pkey = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=180, null=True, blank=True)


    class Meta:
        db_table = 'hostmp'
        verbose_name = '主机模板'

    def __str__(self):
        # 返回的格式
        return self.host
