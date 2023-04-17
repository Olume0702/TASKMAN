from django.shortcuts import render

from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# class TagList(generics.ListCreateAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer

class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskRetrieve(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# class TaskUpdate(generics.UpdateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     # Specify which fields can be updated
#     fields = ('task', 'description', 'tags')

#     def patch(self, request, *args, **kwargs):
#         # Call the parent class's patch() method
#         return super().patch(request, *args, **kwargs)

    
class TaskDestroy(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer