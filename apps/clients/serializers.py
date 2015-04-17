from rest_framework import serializers
from .models import Client, Feed


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client

class ClientMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name']

class ClientFeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feed



