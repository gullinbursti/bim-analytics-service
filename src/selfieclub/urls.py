"""Selfieclub endpoint URL information for Django."""

from django.conf.urls import patterns, url
from selfieclub import views
from rest_framework.urlpatterns import format_suffix_patterns


URL_PATTERNS = patterns('', url(r'^', views.EventView.as_view()))
urlpatterns = format_suffix_patterns(URL_PATTERNS)  # noqa # pylint: disable=invalid-name
