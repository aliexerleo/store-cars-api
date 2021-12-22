from rest_framework import serializers 
from apps.cars.models import Cars
from apps.vans.models import Vans
from apps.trucks.models import Trucks

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'

class VanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vans
        fields = '__all__'

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trucks
        fields = '__all__'

