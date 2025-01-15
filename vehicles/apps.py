from django.apps import AppConfig
import json
import os

class VehiclesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vehicles'

    def ready(self):
        from .models import VehicleType
        try:
            json_file_path = os.path.join(os.path.dirname(__file__), 'vehicle_types.json')
            with open(json_file_path) as f:
                data = json.load(f)
                for type_name in data['vehicle_types']:
                    VehicleType.objects.get_or_create(name=type_name)
        except Exception as e:
            print(f"Error loading vehicle types: {e}")
