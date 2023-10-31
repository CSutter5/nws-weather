import requests
from typing import List

from geopy.geocoders import Nominatim

from .observation import Observation

def current_weather(**kwargs) -> List[Observation]:
    """Get the current weather for a given location

    Raises:
        Exception: Could not get the current weather for the given location

    Returns:
        List[Observation]: A list of observations for the given location
    """
    station = ""

    if 'station' in kwargs:
        station = kwargs['station']
        
    elif 'lat' in kwargs and 'lon' in kwargs:
        lat = kwargs['lat']
        lon = kwargs['lon']
        station = get_station(lat, lon)
        
    elif 'zipcode' in kwargs:
        station = get_station_zipcode(kwargs['zipcode'])
        
    r = requests.get(f"https://api.weather.gov/stations/{station}/observations")
    
    if r.status_code != 200:
        print(r)
        raise Exception(f"Error getting current weather")
    
    observations = []
    
    for d in r.json()['features']:
        observations.append(Observation(d))
        
    return observations

def get_station(lat: float, lon: float) -> str:
    """Find the nearest station to a lat/lon pair

    Args:
        lat (float): Latitude that you want to find the nearest station for
        lon (float): Longitude that you want to find the nearest station for

    Raises:
        Exception: Could not find a station for the lat/lon pair

    Returns:
        str: The nearest station to the lat/lon pair
    """
    
    url = f"https://api.weather.gov/points/{round(lat, 4)},{round(lon, 4)}"
    r = requests.get(url)
    
    if r.status_code == 200:
        observationStationsURL = r.json()['properties']['observationStations']
        observationStationR = requests.get(observationStationsURL)
        
        if observationStationR.status_code == 200:
            return observationStationR.json()['features'][0]['properties']['stationIdentifier']
    
    print(r)
    print(observationStationR)
    raise Exception(f"Error getting station for lat/lon: {lat}, {lon}")
    

def get_station_zipcode(zipcode: str) -> str:
    """Get's the nearest station to a zipcode

    Args:
        zipcode (str): zipcode that you want to find the nearest station for

    Returns:
        str: The nearest station to the zipcode
    """
    
    geolocator = Nominatim(user_agent="zipcode_converter")
    location = geolocator.geocode(zipcode)
    
    return get_station(location.latitude, location.longitude)