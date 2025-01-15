from django.db import models

# Class VehicleType is a model that represents the type of vehicle, such as car, truck, or motorcycle.
class VehicleType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# Class Vehicle is a model that represents a vehicle, such as a car, truck, or motorcycle.
class Vehicle(models.Model):

    name = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # type = models.ForeignKey(VehicleType, on_delete=models.CASCADE) 
    type = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)  
    description = models.TextField(blank=True, null=True)  
    engine = models.CharField(max_length=100, blank=True, null=True) 
    transmission = models.CharField(max_length=100, blank=True, null=True) 
    fuel_type = models.CharField(max_length=50, blank=True, null=True) 
    mileage = models.IntegerField(blank=True, null=True) 
    color = models.CharField(max_length=50, blank=True, null=True)  

    def __str__(self):
        return f"{self.name} ({self.year})"

# TODO: Class Service is a model that represents a service, such as an oil change, tire rotation, or brake inspection.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# TODO: Class Dealer is a model that represents a dealer, such as a car dealership.
class Dealer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# TODO: Class TestDrive is a model that represents a test drive of a vehicle by a customer.
class TestDrive(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField()
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)

    def __str__(self):
        return f"Test Drive for {self.vehicle.name} by {self.customer_name}"