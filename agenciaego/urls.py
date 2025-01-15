from django.contrib import admin
from django.urls import path
from vehicles.views import VehicleViewSet
from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]