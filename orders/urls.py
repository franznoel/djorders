from django.conf.urls import patterns, url

from orders import views

urlpatterns = patterns('',
  url(r'^$', views.orders, name='orders'),
  url(r'transaction/$', views.transaction, name='transaction'),
  url(r'confirmation/$', views.confirmation, name='confirmation'),
)
