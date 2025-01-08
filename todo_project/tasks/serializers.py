from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    completed = serializers.CharField(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'completed', 'created_at']