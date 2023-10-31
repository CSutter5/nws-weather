from NWS_Weather import current_weather, predicted_weather

for weather in current_weather(zipcode="53818"):
    print(weather)


for weather in predicted_weather(gridX=91, gridY=13, gridId='ARX'):
    print(weather)