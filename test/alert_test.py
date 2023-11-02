from NWS_Weather import get_alerts


def test_get_alerts_area():
    # Test get_alerts with area parameter
    result = get_alerts(area='WI')
    assert result is not None
    
def test_get_alerts_lat_long():
    # Test get_alerts with lat and long parameters
    result = get_alerts(lat=42.9104, lon=-89.3853)
    assert result is not None
    
def test_get_alerts_region():
    # Test get_alerts with region parameter
    result = get_alerts(region='GL')
    assert result is not None
    
def test_get_alerts_zone():
    # Test get_alerts with zone parameter
    result = get_alerts(zone='WIZ061')
    assert result is not None
    
def test_get_alerts_region_type():
    # Test get_alerts with region_type parameter
    result = get_alerts(region_type='land')
    assert result is not None
    
def test_get_alerts_zipcode():
    # Test get_alerts with zipcode parameter
    result = get_alerts(zipcode=53575)
    assert result is not None