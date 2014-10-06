"""Project URL configuration."""

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(  # pylint: disable=invalid-name
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^selfieclub/', include('selfieclub.urls')),
)
