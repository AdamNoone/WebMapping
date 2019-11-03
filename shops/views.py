from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop

longitude = -6.2674277
latitude = 53.337154899999994



user_location = Point(longitude, latitude, srid=4326)


class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    template_name = 'shops/index.html'
