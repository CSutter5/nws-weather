from NWS_Weather import current_weather


def test_current_weather_station():
    # Test current_weather with station parameter
    result = current_weather(station='KPVB')
    assert result is not None
    
def test_current_weather_lat_long():
    # Test current_weather with lat and long parameters
    result = current_weather(lat=42.7339, lon=-90.4955)
    assert result is not None
    
def test_current_weather_zipcode():
    # Test current_weather with zipcode parameter
    result = current_weather(zipcode=53818)
    assert result is not None
    