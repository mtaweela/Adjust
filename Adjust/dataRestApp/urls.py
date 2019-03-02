from django.conf.urls import url, include
from dataRestApp import views

urlpatterns = [
    url(r'^performance_metric/$', views.PerformanceMetricView.as_view()),
]
