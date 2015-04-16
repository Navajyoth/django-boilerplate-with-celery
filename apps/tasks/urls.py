from django.conf.urls import patterns, url
from apps.tasks.views import TaskView

urlpatterns = patterns('',
                       url(r'^$', TaskView.as_view(), name='task_list'),
                       )
