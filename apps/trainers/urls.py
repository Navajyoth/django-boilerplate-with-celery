from django.conf.urls import patterns, url

from apps.trainers import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),



    )