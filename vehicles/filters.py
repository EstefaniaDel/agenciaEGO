import django_filters
from .models import Vehicle

class VehicleFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte') 
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')  
    type = django_filters.CharFilter(field_name="type", lookup_expr='iexact')  
    year = django_filters.NumberFilter(field_name="year", lookup_expr='exact') 

    class Meta:
        model = Vehicle
        fields = ['min_price', 'max_price', 'type', 'year']  