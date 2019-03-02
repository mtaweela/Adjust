# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from dataRestApp import models

admin.site.register(models.AdvertisingChannel)
admin.site.register(models.Country)
admin.site.register(models.OperatingSystem)
admin.site.register(models.PerformanceMetric)
