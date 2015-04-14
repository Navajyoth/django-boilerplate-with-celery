from django.conf.urls import patterns, url
<<<<<<< HEAD

from apps.clients import views 

urlpatterns= patterns('',
    url(r'^$', views.home),
    )
=======
from apps.clients import views

urlpatterns = patterns('',
                       url(r'^$', views.home),
                       )
>>>>>>> origin
