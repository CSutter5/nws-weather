import unittest
from NWS_Weather import current_weather, predicted_weather

class TestNWSWeather(unittest.TestCase):
    
    def test_current_weather_station(self):
        # Test current_weather with station parameter
        result = current_weather(station='KPVB')
        self.assertIsNotNone(result)
        
    def test_current_weather_lat_long(self):
        # Test current_weather with lat and long parameters
        result = current_weather(lat=42.7339, lon=-90.4955)
        self.assertIsNotNone(result)
        
    def test_current_weather_zipcode(self):
        # Test current_weather with zipcode parameter
        result = current_weather(zipcode=53818)
        self.assertIsNotNone(result)
        
    def test_predicted_weather_gridId(self):
        # Test predicted_weather with gridId parameter
        result = predicted_weather(gridId='MKX', gridX=38, gridY=57)
        self.assertIsNotNone(result)
        
    def test_predicted_weather_lat_long(self):
        # Test predicted_weather with lat and long parameters
        result = predicted_weather(lat=42.9104, lon=-89.3853)
        self.assertIsNotNone(result)
        
    def test_predicted_weather_zipcode(self):
        # Test predicted_weather with zipcode parameter
        result = predicted_weather(zipcode=53575)
        self.assertIsNotNone(result)
        
if __name__ == '__main__':
    unittest.main()