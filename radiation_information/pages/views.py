from django.shortcuts import render
from django.views import View
from radiation_measurement.models import Radiation_measurement, Type


# Create your views here.

class Index(View):
    def get(self, request):
        type = Type.objects.all()
        type_req = request.GET.get('type')
        if type_req:
            radiation = Radiation_measurement.all_radiation_by_typeId(type_req)

        else:
            radiation = Radiation_measurement.objects.all()

        dict = {
            'types': type,
            'radiations': radiation
        }

        return render(request, 'pages/index.html', dict)
