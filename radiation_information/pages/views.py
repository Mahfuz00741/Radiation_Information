from django.shortcuts import render
from django.views import View
from radiation_measurement.models import Radiation_measurement
from place.models import Place

# Create your views here.

class Index(View):
    def get(self, request):
        place = Place.objects.all()
        place_req = request.GET.get('place')
        if place_req:
            radiation = Radiation_measurement.all_radiation_by_placeId(place_req)

        else:
            radiation = Radiation_measurement.objects.all()

        dict = {
            'places': place,
            'radiations': radiation
        }

        return render(request, 'pages/index.html', dict)
