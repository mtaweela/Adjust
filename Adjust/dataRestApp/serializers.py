from rest_framework import serializers

from dataRestApp import models

""" PerformanceMetric """


class PerformanceMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PerformanceMetric
        fields = '__all__'
        depth = 1
