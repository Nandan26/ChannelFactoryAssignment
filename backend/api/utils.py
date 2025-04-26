import math
import requests
from django.conf import settings

def get_geoloc(address: str) -> dict | None:
    """
    Gets the lat and long of location

    Args:
        address: input address string

    Returns:
        The dictionary with lat, long and formatted address
    """          
    response = requests.get(
        "https://maps.googleapis.com/maps/api/geocode/json",
        params={"address": address, "key": settings.GOOGLE_MAPS_API_KEY}
    )

    if response.status_code == 200 :
        resp_data = response.json()

        if resp_data["status"] != "OK":
            return {
                "valid_input": False,
                "success": False
            }

        result = resp_data["results"][0]
        coords = result["geometry"]["location"]
        formatted = result["formatted_address"]
        
        return {
            "success": True,
            "lat": coords["lat"], 
            "long":coords["lng"],
            "address": formatted
        }
    
    else:
        return {
            "valid_input": True,
            "success": False
        }

def calc_distance(coord1: tuple, coord2: tuple) -> float:
    """
    Calculates the distance between two points using the Haversine formula.

    Args:
        coord1: Latitude of the first point in degrees.
        coord2: Longitude of the first point in degrees.

    Returns:
        The distance between the two points in kms.
    """
    R = 6371

    lat1, lon1 = coord1
    lat2, lon2 = coord2

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Calculate the differences in latitude and longitude and convert it to radians
    diff_lat = lat2_rad - lat1_rad
    diff_lon = lon2_rad - lon1_rad

    # Haversine formula
    a = math.sin(diff_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(diff_lon / 2) ** 2
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distance = R * c

    return distance