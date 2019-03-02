from rest_framework import serializers

from dataRestApp import models


""" AdvertisingChannel """


class AdvertisingChannelSerializer(CustomModelSerializer):
    class Meta:
        model = models.AdvertisingChannel
        fields = '__all__'


""" Country """


class CountrySerializer(CustomModelSerializer):
    class Meta:
        model = models.Country
        fields = '__all__'


""" OperatingSystem """


class OperatingSystemSerializer(CustomModelSerializer):
    class Meta:
        model = models.OperatingSystem
        fields = '__all__'


""" PerformanceMetric """


class PerformanceMetricSerializer(CustomModelSerializer):
    class Meta:
        model = models.PerformanceMetric
        fields = '__all__'
