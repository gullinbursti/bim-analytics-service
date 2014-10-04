from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(  # pylint: disable=invalid-name
    '',
    # Examples:
    # url(r'^$', 'bimanalytics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
