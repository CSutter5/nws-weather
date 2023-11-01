import requests
from typing import List

from geopy.geocoders import Nominatim

from .forcast import forcast

def predicted_weather(**kwargs) -> List[forcast]:
    """Get the predicted weather for a given location

    Raises:
        Exception: Argument Error, gets raised if no valid arguments are given
        Exception: Could not get the predicted weather for the given location

    Returns:
        List[forcast]: List of forcasted data points
    """

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
        
    else:
        raise Exception("No valid arguments given\nYou need to either supply a zipcode, lat/lon pair, or a gridId and gridX/Y Pair")
        
    r = requests.get(f"https://api.weather.gov/gridpoints/{grid[0]}/{grid[1]},{grid[2]}/forecast/hourly")
    
    if r.status_code != 200:
        raise Exception(f"Error getting predicted weather\nStatus Code: {r.status_code}\nGrid ID: {grid}, Grid X: {grid[1]}, Grid Y: {grid[2]}")
    
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

    raise Exception(f"Error getting forecast grid\nStatus Code: {r.status_code}\nLat: {lat}, Lon: {lon}")
    

def get_forecast_grid_zipcode(zipcode: str) ->  (str, int, int):
    
    geolocator = Nominatim(user_agent="zipcode_converter")
    location = geolocator.geocode(zipcode)
    
    return get_forecast_grid(location.latitude, location.longitude)