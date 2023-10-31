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

class Observation:
    timestamp: datetime
    
    rawMessage: str
    textDescription: str
    icon: str
    presentWeather: PresentWeather
    
    temperature: float
    dewpoint: float
    windDirection: str
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
        
        self.rawMessage = data['properties']['rawMessage']
        self.textDescription = data['properties']['textDescription']
        self.icon = data['properties']['icon']
        self.presentWeather = PresentWeather(data['properties']['presentWeather'])
        
        self.temperature = data['properties']['temperature']['value']
        self.dewpoint = data['properties']['dewpoint']['value']
        self.windDirection = data['properties']['windDirection']['value']
        self.windSpeed = data['properties']['windSpeed']['value']
        self.windGust = data['properties']['windGust']['value']
        self.barometricPressure = data['properties']['barometricPressure']['value']
        self.seaLevelPressure = data['properties']['seaLevelPressure']['value']
        self.visibility = data['properties']['visibility']['value']
        self.maxTemperatureLast24Hours = data['properties']['maxTemperatureLast24Hours']['value']
        self.minTemperatureLast24Hours = data['properties']['minTemperatureLast24Hours']['value']
        self.precipitationLastHour = data['properties']['precipitationLastHour']['value']
        self.precipitationLast3Hours = data['properties']['precipitationLast3Hours']['value']
        self.precipitationLast6Hours = data['properties']['precipitationLast6Hours']['value']
        self.relativeHumidity = data['properties']['relativeHumidity']['value']
        self.windChill = data['properties']['windChill']['value']
        self.heatIndex = data['properties']['heatIndex']['value']
        
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