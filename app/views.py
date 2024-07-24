
from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import User, GlucoseLevel
from .serializers import (
  GlucoseLevelSerializer,
)

# Glucoselevelview
class GlucoseLevelCreateView(generics.CreateAPIView):
    queryset = GlucoseLevel.objects.all()
    serializer_class = GlucoseLevelSerializer

    def perform_create(self, serializer):
        glucose_level = serializer.save()
        detail_serializer = GlucoseLevelSerializer(glucose_level)
        return Response(detail_serializer.data)
    

class GlucoseLevelListView(generics.ListAPIView):
    queryset = GlucoseLevel.objects.all()
    serializer_class = GlucoseLevelSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,SearchFilter)
    filterset_fields = ['user__id', 'timestamp']
    ordering_fields = ['timestamp', 'glucose_value']
    search_fields = ['user__id']


class GlucoseLevelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GlucoseLevel.objects.all()
    serializer_class = GlucoseLevelSerializer
