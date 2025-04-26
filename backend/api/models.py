from django.db import models

class LocationModel(models.Model):
    user_input = models.CharField(unique=True)
    formatted_add = models.CharField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class DistanceModel(models.Model):
    origin = models.ForeignKey(LocationModel, related_name='origin_loc', on_delete=models.CASCADE)
    dest = models.ForeignKey(LocationModel, related_name='dest_loc', on_delete=models.CASCADE)
    distance_km = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)