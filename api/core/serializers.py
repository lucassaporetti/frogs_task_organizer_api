from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['uuid', 'status', 'name', 'date', 'time', 'task_type', 'priority']
