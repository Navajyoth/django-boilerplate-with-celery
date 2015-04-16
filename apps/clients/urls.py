from django.conf.urls import patterns, url

from apps.clients.views import ClientListView

urlpatterns= patterns('',
    url(r'^$', ClientListView.as_view(),name='client_index'),
    )
