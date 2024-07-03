from rest_framework import serializers
from .models import ProgramAudience, InventoryAvailability

class ProgramAudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramAudience
        fields = '__all__'

class InventoryAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryAvailability
        fields = '__all__'
