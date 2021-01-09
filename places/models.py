from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    short_description = models.TextField(verbose_name='Короткое описание', blank=True)
    long_description = models.TextField(verbose_name='Полное описание', blank=True)
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title
