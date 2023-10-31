from datetime import datetime

class forcast:
    startTime: datetime
    endTime: datetime
    
    isDaytime: bool
    temperature: float
    temperatureTrend: str
    probabilityOfPrecipitation: int
    dewPoint: float
    windSpeed: int
    windDirection: str
    
    icon: str
    shortForecast: str
    detailedForecast: str
    
    def __init__(self, data: dict):
        """ Initizes the forcast class

        Args:
            data (dict): Data from the NWS API
        """
        
        self.startTime = datetime.strptime(data['startTime'], "%Y-%m-%dT%H:%M:%S%z")
        self.endTime = datetime.strptime(data['endTime'], "%Y-%m-%dT%H:%M:%S%z")
        
        self.isDaytime = data['isDaytime']
        self.temperature = data['temperature']
        self.temperatureTrend = data['temperatureTrend']
        self.probabilityOfPrecipitation = data['probabilityOfPrecipitation']["value"]
        self.dewPoint = data['dewpoint']["value"]
        self.windSpeed = int(data['windSpeed'].split(" ")[0])
        self.windDirection = data['windDirection']
        
        self.icon = data['icon']
        self.shortForecast = data['shortForecast']
        self.detailedForecast = data['detailedForecast']
        
        
    def __str__(self):
        return f"""{self.startTime} - {self.endTime}
{self.shortForecast}
{self.detailedForecast}
Temperature: {self.temperature}°F
Temperature Trend: {self.temperatureTrend}
Probability of Precipitation: {self.probabilityOfPrecipitation}%
Dew Point: {self.dewPoint}°F
Wind Speed: {self.windSpeed} mph
Wind Direction: {self.windDirection}
"""