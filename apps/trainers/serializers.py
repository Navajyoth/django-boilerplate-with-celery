from rest_framework import serializers
from .models import Trainer


class TrainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainer
        # name = Trainer.name
        # fields = ['first_name', 'last_name', 'email', 'photo', 'mobile', 'gender', 'dob', 'created',]