from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from .models import Vehicle
from .serializers import VehicleSerializer
from django_filters.rest_framework import DjangoFilterBackend   
from .filters import VehicleFilter
    
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter] 
    filterset_class = VehicleFilter
    ordering_fields = ['price', 'year']

    def list(self, request):
        """GET all vehicles"""
        vehicles = self.filter_queryset(self.get_queryset())
        serializer = self.serializer_class(vehicles, many=True)
        return Response(serializer.data)

    def create(self, request):
        """POST a new vehicle"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """GET a vehicle by ID"""
        try:
            vehicle = self.queryset.get(pk=pk)
        except Vehicle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(vehicle)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """PUT (update) a vehicle by ID"""
        try:
            vehicle = self.queryset.get(pk=pk)
        except Vehicle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """DELETE a vehicle by ID"""
        try:
            vehicle = self.queryset.get(pk=pk)
        except Vehicle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)