from django.conf.urls import patterns, url
from apps.feeds.views import FeedViewSet
from rest_framework.routers import DefaultRouter

from apps.feeds import views

router = DefaultRouter()
router.register(r'feeds', views.FeedViewSet)

urlpatterns = patterns('',
                       # url(
                       #     r'clients/(?P<client_id>\d+)/feeds/$',
                       #     views.feed_list, name='client_feed_list_per_day'),
                       )
urlpatterns  += router.urls