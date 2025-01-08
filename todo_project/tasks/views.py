from django.shortcuts import render

from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from datetime import date

# Create your views here.

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        today = date.today()
        tasks = Task.objects.all()

        categorized_tasks = {
            'Incoming': tasks.filter(due_date__gt=today),
            'Today': tasks.filter(due_date=today),
            'Overdue': tasks.filter(due_date__lt=today)
        }

        return categorized_tasks

class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer