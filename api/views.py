from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import generics
from . import serializers
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

class QueueList(generics.ListAPIView):
    queryset = Queue.objects.all()
    serializer_class = serializers.QueueSerializer

class QueueDetail(generics.RetrieveAPIView):
    queryset = Queue.objects.all()
    serializer_class = serializers.QueueSerializer

#@login_required
#@group_required('Оператор электронной очереди')
def index(request):
    num_cabinets = Cabinet.objects.all().count()
    num_queues = Queue.objects.all().count()

    return render(
        request,
        'index.html',
        context = {
            'num_cabinets':num_cabinets, 'num_queues':num_queues
        }
    )