from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from . import serializers
from .permissions import IsOwnerOrReadOnly
from equeueapp.models import Cabinet, Queue


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class CabinetList(generics.ListAPIView):
    queryset = Cabinet.objects.all()
    serializer_class = serializers.CabinetSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class QueueList(generics.ListAPIView):
    queryset = Queue.objects.all()
    serializer_class = serializers.QueueSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class QueueDetail(generics.RetrieveAPIView):
    queryset = Queue.objects.all()
    serializer_class = serializers.QueueSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
