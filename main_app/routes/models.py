from django.db import models
from math import radians, sin, cos, sqrt, atan2

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()



class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    #Calculate distance between two cities using latitude and longitude `Haversine formula`.
    def distance_to(self, other_city):
        # approximate radius of earth in km
        R = 6373.0

        lat1 = radians(self.latitude)
        lon1 = radians(self.longitude)
        lat2 = radians(other_city.latitude)
        lon2 = radians(other_city.longitude)

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        #Haversine formula
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance_km = R * c
        return distance_km

class Route(models.Model):
    cities = models.ManyToManyField(City)
