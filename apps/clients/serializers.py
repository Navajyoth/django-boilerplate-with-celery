from rest_framework import serializers
from .models import Client, Feed


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client

class ClientFeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feed



