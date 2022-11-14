from rest_framework import serializers
from django.contrib.auth.models import User
from equeueapp.models import Cabinet, Queue

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = ['id', 'cabinetid', 'name']

class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = ['id', 'queueid', 'cabinetid', 'priority']