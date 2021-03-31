from django.db import models


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Radiation_measurement(models.Model):
    place = models.CharField(max_length=100)
    area = models.CharField(max_length=40)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
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
    def all_radiation_by_typeId(type_id):
        if type_id:
            return Radiation_measurement.objects.filter(type=type_id)

        return Radiation_measurement.objects.all()
