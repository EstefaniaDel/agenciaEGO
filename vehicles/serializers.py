from rest_framework import serializers
from .models import Vehicle, Service, Dealer, TestDrive

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = '__all__'

class TestDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDrive
        fields = '__all__'