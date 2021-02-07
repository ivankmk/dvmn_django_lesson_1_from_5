import requests
from io import BytesIO
import os
from urllib.parse import urlparse
from django.core.management.base import BaseCommand
from places.models import Image, Place


class InsufficientDataError(Exception):
    """Class of insufficient data"""
    pass


class Command(BaseCommand):
    help = 'Adding the additional places into the database.'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='URL for .json file.')

    def load_place(self, place_details):
        title = place_details.get('title')
        latitude = place_details.get('coordinates', {}).get('lat')
        longitude = place_details.get('coordinates', {}).get('lng')

        if not any([title, latitude, longitude]):
            raise InsufficientDataError(
                'Insufficient data - check title, lat and long')

        short_description = place_details.get('description_short', '')
        long_description = place_details.get('description_long', '')

        place_to_load = {
            'title': title,
            'latitude': latitude,
            'longitude': longitude,
            'short_description': short_description,
            'long_description': long_description
        }

        place, created = Place.objects.get_or_create(
            title=title,
            defaults=place_to_load
        )
        print(f'Place saved: {title}')
        return place

    def load_place_images(self, image_urls, place):
        for image_url in image_urls:
            image = Image.objects.create(place=place)
            response = requests.get(image_url)
            response.raise_for_status()
            image_content = response.content
            image.image.save(
                os.path.basename(urlparse(image_url).path),
                BytesIO(image_content)
            )
            print(f'Image saved: {image_url}')

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()
        place_details = response.json()
        place = self.load_place(place_details)
        image_urls = place_details.get('imgs', [])
        self.load_place_images(image_urls, place)
