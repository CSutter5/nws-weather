# Python NWS Weather Package

This Python package provides a simple interface for retrieving weather data from the National Weather Service (NWS) API.

## Installation

To install this package, simply run the following command:

```pip install nws-weather```

## Usage
First, import the package:

```python
from NWS_Weather import current_weather, predicted_weather
```

To get the current weather for a given location, use the ```current_weather``` function:

```python
weather = current_weather(station='KJFK')
weather = current_weather(lat=40.64, lon=-73.76)
weather = current_weather(zipcode=11430)

for w in weather:
    print(w)
```

To get the predicted weather for a given location, use the ```predicted_weather``` function:

```python
weather = predicted_weather(gridX=91, gridY=13, gridId='ARX')
weather = predicted_weather(lat=40.64, lon=-73.76)
weather = predicted_weather(zipcode=11430)

for w in weather:
    print(w)
```

Station is the NWS observation station ID. You can find the station ID for your location [here](https://w1.weather.gov/xml/current_obs/seek.php?state=ny&Find=Find). </br>
Lat, Lon is the latitude and longitude of the location you want the weather for. </br>
Zipcode is the zipcode of the location you want the weather for. </br>
GridX, GridY, GridId is the grid coordinates and ID of the location you want the weather for. </br>