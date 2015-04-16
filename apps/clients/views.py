from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework import generics

from apps.clients.serializers import ClientSerializer
from apps.clients.models import Client, Feed


# def home(request):
#     return HttpResponse('site under construction')

class ClientListView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
