from django.conf.urls import patterns, url, include


from apps.clients import views
from rest_framework import renderers
# from rest_framework import ViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clients', views.ClientViewSet)


urlpatterns = patterns('',
                       url(
                           r'^clients/(?P<client_id>\d+)/tasks/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/$',
                           views.client_task_list, name='client-task-list-per-day'),
                       )
urlpatterns += router.urls
