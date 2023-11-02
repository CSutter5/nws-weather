import requests
from typing import List, Tuple

from geopy.geocoders import Nominatim

from .alert import alert

# This get alert information from the NWS API
# https://api.weather.gov/alerts/active?area=CA
# 
# Need method for getting alerts with an area, with a point (lat, lon), with a region, with a zone, could be region_type (land, marine), zipcode
# https://api.weather.gov/alerts/active?
# 

def get_alerts(**kwargs) -> List[alert]:
    """Get active alerts for a given location
    
    Raises:
        Exception: Invalid region given
        Exception: Invalid region type given
        Exception: No valid arguments given
        Exception: Error getting alerts

    Returns:
        List[alert]: _description_
    """

    base_url = "https://api.weather.gov/alerts/active"
    request_url = base_url

    if "area" in kwargs:
        request_url = f"{request_url}?area={kwargs['area']}"
    
    elif "lat" in kwargs and "lon" in kwargs:
        request_url = f"{base_url}?point={kwargs['lat']},{kwargs['lon']}"
    
    elif "region" in kwargs:
        if not kwargs["region"] in ["AL", "AT", "GL", "GM", "PA", "PI"]:
            raise Exception(f"Invalid region given: {kwargs['region']}\nValid regions are: AL, AT, GL, GM, PA, PI")
        
        request_url = f"{base_url}?region={kwargs['region']}"
    
    elif "zone" in kwargs:
        request_url = f"{base_url}?zone={kwargs['zone']}"
    
    elif "region_type" in kwargs:
        if not kwargs["region_type"] in ["land", "marine"]:
            raise Exception(f"Invalid region type given: {kwargs['region_type']}\nValid region types are: land, marine")
        
        request_url = f"{base_url}?region_type={kwargs['region_type']}"
        
    elif "zipcode" in kwargs:
        lat, lon = zipcode_to_lat_lon(kwargs["zipcode"])
        request_url = f"{base_url}?point={lat},{lon}"
    
    else:
        raise Exception("No valid arguments given\nYou need to either supply a area, lat/lon pair, region, zone_id, or region_type")
    

    r = requests.get(request_url)

    if r.status_code != 200:
        raise Exception(f"Error getting alerts\nStatus Code: {r.status_code}")
    
    alerts = []
    
    for d in r.json()["features"]:
        alerts.append(alert(d))
    
    return alerts

def zipcode_to_lat_lon(zipcode: int) -> Tuple[int, int]:
    """Convert a zipcode to a lat/lon pair

    Args:
        zipcode (int): the zipcode to convert

    Returns:
        Tuple[int, int]: the lat/lon pair
    """

    geolocator = Nominatim(user_agent="zipcode_converter")
    location = geolocator.geocode(zipcode)
    
    return (location.latitude, location.longitude)
    
    