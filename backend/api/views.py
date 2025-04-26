from django.db.models import Q
from rest_framework import views, status
from .serializers import LocationInpSerializer
from rest_framework.response import Response
from .utils import get_geoloc, calc_distance
from .models import LocationModel, DistanceModel

# Create your views here.
class DistanceView(views.APIView):
    def post(self, request):
        try:

            input = LocationInpSerializer(data=request.data)

            if not input.is_valid():
                return Response(input.errors, status=status.HTTP_400_BAD_REQUEST)
            
            origin = input.validated_data["origin"]
            destination = input.validated_data["destination"]
            origin_inp = origin.lower()
            destination_inp = destination.lower()

            # check from db if location already exist 
            origin_loc = LocationModel.objects.filter(user_input = origin_inp.lower()).first()

            dest_loc = LocationModel.objects.filter(user_input = destination_inp.lower()).first()

            location_exists = True
            # insert origin location into db if not already exist
            if not origin_loc:
                location_exists = False
                origin_data = get_geoloc(origin_inp)

                if not origin_data["success"]:

                    if not origin_data["valid_input"]:
                        return Response(
                            {
                                "error": f"Unable to find place with name '{origin}' please enter correct location"
                            },
                            status=status.HTTP_400_BAD_REQUEST
                        )
                    else:
                        return Response(
                            {
                                "error": "Error while fetching location"
                            },
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR
                        )

                origin_loc = LocationModel.objects.create(
                    user_input = origin_inp.lower(),
                    formatted_add = origin_data.get("address"),
                    latitude = origin_data.get("lat"),
                    longitude = origin_data.get("long")
                )

            # insert destination loc into db if not already exists
            if not dest_loc:
                location_exists = False
                dest_data = get_geoloc(destination_inp)

                if not dest_data["success"]:
                    if not dest_data["valid_input"]:
                        return Response(
                            {
                                "error": f"Unable to find place with name '{destination}' please enter correct location"
                            },
                            status=status.HTTP_400_BAD_REQUEST
                        )
                    
                    else:
                        return Response(
                            {
                                "error": "Error while fetching location"
                            },
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR
                        )

                dest_loc = LocationModel.objects.create(
                    user_input = destination_inp.lower(),
                    formatted_add = dest_data.get("address"),
                    latitude = dest_data.get("lat"),
                    longitude = dest_data.get("long")
                )
                
            # fetch distance data from db only if location already exists
            distance_data = None

            if location_exists:
                distance_data = DistanceModel.objects.filter(origin = origin_loc, dest = dest_loc).first()

            if not distance_data:
                
                coord1 = (origin_loc.latitude, origin_loc.longitude)
                coord2 = (dest_loc.latitude, dest_loc.longitude)

                dist_km = calc_distance(coord1, coord2)

                distance_data = DistanceModel.objects.create(
                    origin = origin_loc,
                    dest = dest_loc,
                    distance_km = dist_km
                )

            return Response({
                "origin": origin_loc.formatted_add,
                "destination": dest_loc.formatted_add,
                "distance_km": round(distance_data.distance_km, 2)
            })
        
        except Exception as err:
            return Response(
                {
                    "error": str(err)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )