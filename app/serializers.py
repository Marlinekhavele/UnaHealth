from rest_framework import serializers
from .models import  GlucoseLevel



class GlucoseLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlucoseLevel
        fields = '__all__'
