from django.conf.urls import patterns, url

from apps.trainers.views import TrainerListView

urlpatterns = patterns('',
    url(r'^$', TrainerListView.as_view(), name='home'),



    )