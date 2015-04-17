from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework import generics

from apps.clients.serializers import ClientSerializer
from apps.clients.models import Client, Feed

from rest_framework import viewsets


# def home(request):
#     return HttpResponse('site under construction')


class ClientViewSet(viewsets.ModelViewSet):
    queryset =Client.objects.all()
    serializer_class=ClientSerializer

    
    # permission_classes = (permissions.ISAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    # @detail_route(render_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request,*args, **kwargs):
    #     client =self.get_object()
    #     return Response(clients.highlighted)

    # def perform_create(self.serializer):
    #     serializer.save(owner=self.request.user)



# class ClientListView(generics.ListCreateAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
