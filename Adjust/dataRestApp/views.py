# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response

from dataRestApp import models
from dataRestApp import serializers


class PerformanceMetricView(APIView):
    def get(self, request):
        # filter
        date_from = request.query_params.get('date_from', False)
        date_to = request.query_params.get('date_to', False)

        performance_metrics = []
        if date_from:
            performance_metrics = models.PerformanceMetric.objects.filter(
                date__gte=date_from)

        if date_to:
            performance_metrics = performance_metrics.filter(
                date__lte=date_to)

        filter_by_channel = request.query_params.get(
            'filter_by_channel', False)
        if filter_by_channel:
            performance_metrics = performance_metrics.filter(
                advertising_channel__name=filter_by_channel)

        filter_by_country = request.query_params.get(
            'filter_by_country', False)
        if filter_by_country:
            performance_metrics = performance_metrics.filter(
                country__name=filter_by_country)

        filter_by_OS = request.query_params.get(
            'filter_by_OS', False)
        if filter_by_OS:
            performance_metrics = performance_metrics.filter(
                operating_system__name=filter_by_OS)

        # sort
        sort_by = request.query_params.get('sort_by', False)
        if sort_by:
            sort_type = request.query_params.get('sort_type', False)
            if sort_type == 'asc':
                performance_metrics = performance_metrics.order_by(sort_by)
            else:
                performance_metrics = performance_metrics.order_by(
                    '-' + sort_by)

        # group_by
        group_by = request.query_params.get('group_by', False)

        if group_by:
            group_by_arr = group_by.split(',')
            performance_metrics = performance_metrics.values(
                *group_by_arr)
            return Response(
                performance_metrics
            )

        return Response(
            serializers.PerformanceMetricSerializer(
                performance_metrics, many=True).data
        )
