from datetime import datetime


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

class forcast:
    start_time: datetime
    end_time: datetime
    
    is_daytime: bool
    temperature: float
    temperature_trend: str
    probability_of_precipitation: int
    dew_point: float
    wind_speed: int
    wind_direction: str
    
    icon: str
    short_forecast: str
    detailed_forecast: str
    
    def __init__(self, data: dict):
        """ Initizes the forcast class

        Args:
            data (dict): Data from the NWS API
        """
        
        self.start_time = datetime.strptime(data['startTime'], "%Y-%m-%dT%H:%M:%S%z")
        self.end_time   = datetime.strptime(data['endTime'], "%Y-%m-%dT%H:%M:%S%z")
        
        self.is_daytime                     = check_if_none(data['isDaytime'])
        self.temperature                    = check_if_none(data['temperature'])
        self.temperature_trend              = check_if_none(data['temperatureTrend'])
        self.probability_of_precipitation   = check_if_none(data['probabilityOfPrecipitation']["value"])
        self.dew_point                      = check_if_none(data['dewpoint']["value"])
        self.wind_speed                     = int(data['windSpeed'].split(" ")[0])
        self.wind_direction                 = check_if_none(data['windDirection'])
        
        self.icon = data['icon']
        self.short_forecast = data['shortForecast']
        self.detailed_forecast = data['detailedForecast']
        
        
    def __str__(self):
        return f"""{self.start_time} - {self.end_time}
{self.short_forecast}
{self.detailed_forecast}
Temperature: {self.temperature}°F
Temperature Trend: {self.temperature_trend}
Probability of Precipitation: {self.probability_of_precipitation}%
Dew Point: {self.dew_point}°F
Wind Speed: {self.wind_speed} mph
Wind Direction: {self.wind_direction}
"""