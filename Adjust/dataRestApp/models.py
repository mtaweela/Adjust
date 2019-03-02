# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class AdvertisingChannel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OperatingSystem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PerformanceMetric(models.Model):
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.FloatField()
    revenue = models.FloatField()
    date = models.DateField()
    advertising_channel = models.ForeignKey(AdvertisingChannel)
    country = models.ForeignKey(Country)
    operating_system = models.ForeignKey(OperatingSystem)
