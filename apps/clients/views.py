import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets


from apps.clients.serializers import ClientSerializer
from apps.feeds.serializers import FeedSerializer
from apps.tasks.serializers import TaskSerializer
from apps.clients.models import Client
from apps.tasks.models import Task


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def client_task_list(request, client_id, year=None, month=None, day=None):
    client = get_object_or_404(Client, id=client_id)
    date = datetime.date(int(year), int(month), int(day))
    if year:
        client_tasks_of_day = client.tasks.filter(date=date).order_by('index')
    print client_tasks_of_day
    serializer = TaskSerializer(client_tasks_of_day, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def client_feed_list(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client_feed = client.feeds.order_by('datetime')
    serializer = FeedSerializer(client_feed, many=True)
    return Response(serializer.data)
