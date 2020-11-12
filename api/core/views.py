from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet, RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_object(self):
        return Task.objects.get()


# Create your views here.
