
from django.urls import path
from .views import DistanceView

urlpatterns = [
    path("calc/distance/", DistanceView.as_view(), name="calculate-distance")
]