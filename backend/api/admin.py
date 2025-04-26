from django.contrib import admin

# Register your models here.
from .models import LocationModel, DistanceModel

admin.site.register(LocationModel)
admin.site.register(DistanceModel)