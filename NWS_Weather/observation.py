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

def checkIfNone(value):
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
    
    rawMessage: str
    textDescription: str
    icon: str
    presentWeather: PresentWeather
    
    temperature: float
    dewpoint: float
    windDirection: int
    windSpeed: float
    windGust: float
    barometricPressure: float
    seaLevelPressure: float
    visibility: float
    maxTemperatureLast24Hours: float
    minTemperatureLast24Hours: float
    precipitationLastHour: float
    precipitationLast3Hours: float
    precipitationLast6Hours: float
    relativeHumidity: float
    windChill: float
    heatIndex: float
    
    cloudLayers: CloudLayers
    
    
    def __init__(self, data: dict):
        """ Initizes the observation class

        Args:
            data (dict): Data from the NWS API
        """
        
        self.timestamp = datetime.strptime(data['properties']['timestamp'], "%Y-%m-%dT%H:%M:%S%z")
        
        self.rawMessage = checkIfNone(data['properties']['rawMessage'])
        self.textDescription = checkIfNone(data['properties']['textDescription'])
        self.icon = checkIfNone(data['properties']['icon'])
        self.presentWeather = PresentWeather(data['properties']['presentWeather'])
        
        self.temperature = checkIfNone(data['properties']['temperature']['value'])
        self.dewpoint = checkIfNone(data['properties']['dewpoint']['value'])
        self.windDirection = checkIfNone(data['properties']['windDirection']['value'])
        self.windSpeed = checkIfNone(data['properties']['windSpeed']['value'])
        self.windGust = checkIfNone(data['properties']['windGust']['value'])
        self.barometricPressure = checkIfNone(data['properties']['barometricPressure']['value'])
        self.seaLevelPressure = checkIfNone(data['properties']['seaLevelPressure']['value'])
        self.visibility = checkIfNone(data['properties']['visibility']['value'])
        self.maxTemperatureLast24Hours = checkIfNone(data['properties']['maxTemperatureLast24Hours']['value'])
        self.minTemperatureLast24Hours = checkIfNone(data['properties']['minTemperatureLast24Hours']['value'])
        self.precipitationLastHour = checkIfNone(data['properties']['precipitationLastHour']['value'])
        self.precipitationLast3Hours = checkIfNone(data['properties']['precipitationLast3Hours']['value'])
        self.precipitationLast6Hours = checkIfNone(data['properties']['precipitationLast6Hours']['value'])
        self.relativeHumidity = checkIfNone(data['properties']['relativeHumidity']['value'])
        self.windChill = checkIfNone(data['properties']['windChill']['value'])
        self.heatIndex = checkIfNone(data['properties']['heatIndex']['value'])
        
        self.cloudLayers = CloudLayers(data['properties']['cloudLayers'])
        
        
    def __str__(self):
        return f"""{self.timestamp}

{self.rawMessage}
{self.textDescription}
{self.icon}
{self.presentWeather}

Temperature: {self.temperature} C
Dewpoint: {self.dewpoint} C
Wind Direction: {self.windDirection} Deg
Wind Speed: {self.windSpeed} KPH
Wind Gust: {self.windGust} KPH
Barometric Pressure: {self.barometricPressure} pa
Sea Level Pressure: {self.seaLevelPressure} pa
Visibility: {self.visibility} m
Max Temperature Last 24 Hours: {self.maxTemperatureLast24Hours} C
Min Temperature Last 24 Hours: {self.minTemperatureLast24Hours} C
Precipitation Last Hour: {self.precipitationLastHour} mm
Precipitation Last 3 Hours: {self.precipitationLast3Hours} mm
Precipitation Last 6 Hours: {self.precipitationLast6Hours} mm
Relative Humidity: {self.relativeHumidity} %
Wind Chill: {self.windChill} C
Heat Index: {self.heatIndex} C

{self.cloudLayers}"""