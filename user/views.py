
from rest_framework import generics
from rest_framework.response import Response
from .models import User
from .serializers import (
    UserSerializer
)
# Create your views here.

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        detail_serializer = UserSerializer(user)
        return Response(detail_serializer.data)
    

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
   


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




