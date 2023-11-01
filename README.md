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

Station is the NWS observation station ID. You can find the station ID for your location [here](https://w1.weather.gov/xml/currcleaent_obs/seek.php?state=ny&Find=Find). </br>
Lat, Lon is the latitude and longitude of the location you want the weather for. </br>
Zipcode is the zipcode of the location you want the weather for. </br>
GridX, GridY, GridId is the grid coordinates and ID of the location you want the weather for. </br>

### Observation object
The observation object contains the following attributes:

```python
observation.timestamp # datetime object of the observation time

observation.raw_message         # raw message from the NWS API
observation.text_description    # text description of the weather 
observation.icon                # url to icon representing the weather
observation.present_weather     # present weather

observation.temperature                     # the observed temperature
observation.dewpoint                        # the observed dewpoint
observation.wind_direction                  # the observed wind direction
observation.wind_speed                      # the observed wind speed
observation.wind_gust                       # the observed wind gust
observation.barometric_pressure             # the observed barometric pressure
observation.sea_level_pressure              # the observed sea level pressure
observation.visibility                      # the observed visibility
observation.max_temperature_last_24_hours   # the observed max temperature last 24 hours
observation.min_temperature_last_24_hours   # the observed min temperature last 24 hours
observation.precipitation_last_hour         # the observed precipitation last hour
observation.precipitation_last3_hours       # the observed precipitation last 3 hours
observation.precipitation_last6_hours       # the observed precipitation last 6 hours
observation.relative_humidity               # the observed relative humidity
observation.wind_chill                      # the observed wind chill
observation.heat_index                      # the observed heat index

observation.cloud_layers    # the observed cloud layers
```

### Forecast object
The forecast object contains the following attributes:

```python
forcast.start_time  # datetime object of the forcast start time
forcast.end_time    # datetime object of the forcast end time

forcast.is_daytime                      # True if the forcast is for daytime, False if it is for nighttime
forcast.temperature                     # The forcasted temperature
forcast.temperature_trend               # The forcasted temperature trend
forcast.probability_of_precipitation    # The forcasted probability of precipitation
forcast.dew_point                       # The forcasted dew point
forcast.wind_speed                      # The forcasted wind speed
forcast.wind_direction                  # The forcasted wind direction
forcast.icon                            # The icon that represents the forcasted weather

forcast.short_forecast      # The short forcast
forcast.detailed_forecast   # The detailed forcast
```