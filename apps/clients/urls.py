from django.conf.urls import patterns, url

from apps.clients import views 

urlpatterns= patterns('',
    url(r'^$', views.home),
    )
