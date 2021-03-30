from django.db import models
from place.models import Place


# Create your models here.
class Radiation_measurement(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    area = models.CharField(max_length=40)
    type = models.CharField(max_length=50)
    brand = models.CharField(max_length=40)
    measured_value_EF = models.CharField(max_length=10, default='EF V/m', editable=False)
    EF_measured_value = models.CharField(max_length=30)
    measured_value_MF = models.CharField(max_length=10, default='MF μT', editable=False)
    MF_measured_value = models.CharField(max_length=30)
    measured_value_Power = models.CharField(max_length=10, default='Power mW/cm2', editable=False)
    power_measured_value = models.CharField(max_length=30)
    alarm = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=False)

    @staticmethod
    def all_radiation_by_placeId(place_id):
        if place_id:
            return Radiation_measurement.objects.filter(place=place_id)

        return Radiation_measurement.objects.all()
