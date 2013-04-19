from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^djorders/', include('djorders.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^$', 'djorders.views.home', name='home'),
    url(r'^orders/', include('orders.urls', namespace="orders")),
    url(r'^admin/', include(admin.site.urls)),
)
