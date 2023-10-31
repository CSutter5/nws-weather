import requests
from typing import List

from geopy.geocoders import Nominatim

from .forcast import forcast

def predicted_weather(**kwargs) -> List[forcast]:

    grid = ("", 0, 0)

    if 'gridX' in kwargs and 'gridY' in kwargs and 'gridId' in kwargs:
        grid = (
            kwargs['gridId'],
            kwargs['gridX'],
            kwargs['gridY'],
        )
        
    elif 'lat' in kwargs and 'lon' in kwargs:
        lat = kwargs['lat']
        lon = kwargs['lon']
        grid = get_forecast_grid(lat, lon)
        
    elif 'zipcode' in kwargs:
        grid = get_forecast_grid_zipcode(kwargs['zipcode'])
        
    r = requests.get(f"https://api.weather.gov/gridpoints/{grid[0]}/{grid[1]},{grid[2]}/forecast/hourly")
    
    if r.status_code != 200:
        print(r)
        raise Exception(f"Error getting predicted weather")
    
    forcasts = []
    
    for d in r.json()["properties"]["periods"]:
        forcasts.append(forcast(d))
        
    return forcasts    

def get_forecast_grid(lat: int, lon: int) -> (str, int, int):

    url = f"https://api.weather.gov/points/{round(lat, 4)},{round(lon, 4)}"
    r = requests.get(url)
    
    if r.status_code == 200:        
        return (
            r.json()['properties']['gridId'],
            r.json()['properties']['gridX'],
            r.json()['properties']['gridY']
        )

    print(r)
    raise Exception(f"Error getting forecast grid")
    

def get_forecast_grid_zipcode(zipcode: str) ->  (str, int, int):
    
    geolocator = Nominatim(user_agent="zipcode_converter")
    location = geolocator.geocode(zipcode)
    print(location.latitude, location.longitude)
    
    return get_forecast_grid(location.latitude, location.longitude)