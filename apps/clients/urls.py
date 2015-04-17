from django.conf.urls import patterns, url


from apps.clients import views
from rest_framework import renderers
# from rest_framework import ViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clients',views.ClientViewSet)



# client_list = ClientViewSet.as_view({
#     'get':'list'
#     'post':'create'
#     })
# client_detail = ClientViewSet.as_view({
#     'get':'retrieve'
#     'put':'update'
#     'patch':'partial_update'
#     'delete':'destroy'
#     })

urlpatterns = router.urls
# # patterns('',
#     url(r'^$', ClientListView.as_view(),name='client_index'),
#     )
