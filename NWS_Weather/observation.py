from datetime import datetime

class PresentWeather:
    data: str
    
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return ", ".join(self.data)

class CloudLayers:
    layers: list
    
    def __init__(self, layers: list):
        self.layers = layers

    def __str__(self):
        s = "Cloud Layers:"
        
        for i, layer in enumerate(self.layers):
            s += f"""
Layer {i + 1}:
    Amount: {layer['amount']}
    Base: {layer['base']['value']} m
"""
            
        return s

def check_if_none(value):
    """Returns 0 if the value is None

    Args:
        value: Any value you want to check to see if it is None

    Returns:
        0 if the value is None, otherwise the value 
    """
    if value == None:
        return 0
    return value

class Observation:
    timestamp: datetime
    
    raw_message: str
    text_description: str
    icon: str
    present_weather: PresentWeather
    
    temperature: float
    dewpoint: float
    wind_direction: int
    wind_speed: float
    wind_gust: float
    barometric_pressure: float
    sea_level_pressure: float
    visibility: float
    max_temperature_last_24_hours: float
    min_temperature_last_24_hours: float
    precipitation_last_hour: float
    precipitation_last_3_hours: float
    precipitation_last_6_hours: float
    relative_humidity: float
    wind_chill: float
    heat_index: float
    
    cloud_layers: CloudLayers
    
    
    def __init__(self, data: dict):
        """ Initizes the observation class

        Args:
            data (dict): Data from the NWS API
        """
        
        self.timestamp = datetime.strptime(data['properties']['timestamp'], "%Y-%m-%dT%H:%M:%S%z")
        
        self.raw_message        = data['properties']['rawMessage']
        self.text_description   = data['properties']['textDescription']
        self.icon               = data['properties']['icon']
        
        self.temperature                    = check_if_none(data['properties']['temperature']['value'])
        self.dewpoint                       = check_if_none(data['properties']['dewpoint']['value'])
        self.wind_direction                 = check_if_none(data['properties']['windDirection']['value'])
        self.wind_speed                     = check_if_none(data['properties']['windSpeed']['value'])
        self.wind_gust                      = check_if_none(data['properties']['windGust']['value'])
        self.barometric_pressure            = check_if_none(data['properties']['barometricPressure']['value'])
        self.sea_level_pressure             = check_if_none(data['properties']['seaLevelPressure']['value'])
        self.visibility                     = check_if_none(data['properties']['visibility']['value'])
        self.max_temperature_last_24_hours  = check_if_none(data['properties']['maxTemperatureLast24Hours']['value'])
        self.min_temperature_last_24_hours  = check_if_none(data['properties']['minTemperatureLast24Hours']['value'])
        self.precipitation_last_hour        = check_if_none(data['properties']['precipitationLastHour']['value'])
        self.precipitation_last_3_hours      = check_if_none(data['properties']['precipitationLast3Hours']['value'])
        self.precipitation_last_6_hours      = check_if_none(data['properties']['precipitationLast6Hours']['value'])
        self.relative_humidity              = check_if_none(data['properties']['relativeHumidity']['value'])
        self.wind_chill                     = check_if_none(data['properties']['windChill']['value'])
        self.heat_index                     = check_if_none(data['properties']['heatIndex']['value'])
        
        self.present_weather = PresentWeather(data['properties']['presentWeather'])
        self.cloud_layers    = CloudLayers(data['properties']['cloudLayers'])
        
    def __str__(self):
        return f"""{self.timestamp}

{self.raw_message}
{self.text_description}
{self.icon}
{self.present_weather}

Temperature: {self.temperature} C
Dewpoint: {self.dewpoint} C
Wind Direction: {self.wind_direction} Deg
Wind Speed: {self.wind_speed} KPH
Wind Gust: {self.wind_gust} KPH
Barometric Pressure: {self.barometric_pressure} pa
Sea Level Pressure: {self.sea_level_pressure} pa
Visibility: {self.visibility} m
Max Temperature Last 24 Hours: {self.max_temperature_last_24_hours} C
Min Temperature Last 24 Hours: {self.min_temperature_last_24_hours} C
Precipitation Last Hour: {self.precipitation_last_hour} mm
Precipitation Last 3 Hours: {self.precipitation_last_3_hours} mm
Precipitation Last 6 Hours: {self.precipitation_last_6_hours} mm
Relative Humidity: {self.relative_humidity} %
Wind Chill: {self.wind_chill} C
Heat Index: {self.heat_index} C

{self.cloudLayers}"""