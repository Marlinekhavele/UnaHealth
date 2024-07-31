from rest_framework import serializers
from .models import  GlucoseRecord



class GlucoseRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlucoseRecord
        fields = '__all__'
