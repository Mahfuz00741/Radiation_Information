from django.contrib import admin
from .models import Radiation_measurement


# Register your models here.
class Admin_display(admin.ModelAdmin):
    list_display = ['place', 'area', 'type', 'brand', 'EF_measured_value', 'MF_measured_value', 'power_measured_value',
                    'alarm', 'date']


admin.site.register(Radiation_measurement, Admin_display)
