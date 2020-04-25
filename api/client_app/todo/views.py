from rest_framework import viewsets


# Create your views here.

from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
