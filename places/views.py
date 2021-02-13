from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place

# Create your views here.


def get_places(request):
    places = Place.objects.all()
    places_serialized = {"type": "FeatureCollection", "features": []}
    for place in places:
        places_serialized['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse('get_place', args=[place.id])
                }
            }
        )
    return render(request, 'index.html', context={'data': places_serialized})


def get_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    context = {
        "title": place.title,
        "imgs": [
                image.image.url for image in place.images.all()
            ],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }
    return JsonResponse(
        context,
        json_dumps_params={'ensure_ascii': False, 'indent': 4})
