from django.db import models

# Create your models here.

class Garage(models.Model):
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    is_parking_avaliable = models.BooleanField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

garages = Garage.objects.all()
print(garages)

garage = Garage()
garage.location = '박주헌'
garage.capacity = 1818
garage.is_parking_avaliable = True
garage.opening_time = '07:00'
garage.closing_time = '18:00'
garage.save()

garage_2 = Garage.objects.create(location = '강성은', capacity = '1818', is_parking_avaliable = "False", opening_time = '07:00', closing_time = '18:00')

garage_2.delete()