from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers import CarSerializer, VanSerializer, TruckSerializer
from apps.cars.models import Cars
from apps.vans.models import Vans
from apps.trucks.models import Trucks

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes


@permission_classes([IsAuthenticated])
class CarsApiView(APIView):

    def get(self, request):
        cars = Cars.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data )

    def post(self, request):
        cars = CarSerializer(data=request.data)
        cars.is_valid(raise_exception=True)
        cars.save()
        return Response(status=status.HTTP_200_OK, data=cars.data)

@permission_classes([AllowAny])
class VansApiView(APIView):
    def get(self, request):
        vans = Vans.objects.all()
        serializer = VanSerializer(vans, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        serializer = VanSerilaizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)

@permission_classes([AllowAny])
class TrucksApiView(APIView):
    def get(self, request):
        trucks = Trucks.objects.all()
        serializer = TruckSerializer(trucks, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        serializer = TruckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
