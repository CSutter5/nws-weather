from NWS_Weather import predicted_weather


def test_predicted_weather_gridId():
    # Test predicted_weather with gridId parameter
    result = predicted_weather(gridId='MKX', gridX=38, gridY=57)
    assert result is not None
    
def test_predicted_weather_lat_long():
    # Test predicted_weather with lat and long parameters
    result = predicted_weather(lat=42.9104, lon=-89.3853)
    assert result is not None
    
def test_predicted_weather_zipcode():
    # Test predicted_weather with zipcode parameter
    result = predicted_weather(zipcode=53575)
    assert result is not None