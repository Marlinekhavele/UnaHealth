
from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import  GlucoseRecord
from .serializers import (
  GlucoseRecordSerializer,
)

# GlucoseRecordview
class GlucoseRecordCreateView(generics.CreateAPIView):
    queryset = GlucoseRecord.objects.all()
    serializer_class = GlucoseRecordSerializer

    def perform_create(self, serializer):
        glucose_record = serializer.save()
        detail_serializer = GlucoseRecordSerializer(glucose_record)
        return Response(detail_serializer.data)
    

class GlucoseRecordListView(generics.ListAPIView):
    queryset = GlucoseRecord.objects.all()
    serializer_class = GlucoseRecordSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,SearchFilter)
    filterset_fields = ['user_id', 'timestamp']
    ordering_fields = ['timestamp', 'Gerät']
    search_fields = ['user_id']


class GlucoseRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GlucoseRecord.objects.all()
    serializer_class = GlucoseRecordSerializer
