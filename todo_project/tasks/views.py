from django.shortcuts import render

from rest_framework import generics, response
from .models import Task
from .serializers import TaskSerializer
from datetime import date
from rest_framework.response import Response

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        today = date.today()
        queryset = Task.objects.all()
        
        # First group the tasks by their completion status
        incoming_tasks = queryset.filter(due_date__date__gt=today)
        today_tasks = queryset.filter(due_date__date=today)
        overdue_tasks = queryset.filter(due_date__date__lt=today)
        
        # Serialize each group separately
        categorized_tasks = {
            'Incoming': TaskSerializer(incoming_tasks, many=True).data,
            'Today': TaskSerializer(today_tasks, many=True).data,
            'Overdue': TaskSerializer(overdue_tasks, many=True).data
        }
        
        return Response(categorized_tasks)
class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer