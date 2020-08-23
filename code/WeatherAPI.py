# These two lines just because my Python setup can't find the installed "requests" module otherwise
import sys
sys.path.append('C:\\Users\\Helen\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python38\\site-packages')

# Import things actually needed for this
import requests
import json

# Documentation for this API at https://www.weather.gov/documentation/services-web-api

# Pull all JSON data from my grid x and grid y (77,87) in the weather.gov grid system
query = requests.get('https://api.weather.gov/gridpoints/HGX/77,87/forecast/hourly')

# Convert JSON data to dictionaries in Python
alldata = json.loads(query.text)

# Pull out the periods. Each period represents one hour into the future and there are 156!
data = alldata["properties"]["periods"]

# Make a list and append the "short forecast" for each of the next 24 hours (24 periods)
forecast = []
for i in range(24):
    forecast.append(data[i]["shortForecast"])
    print(data[i]["shortForecast"])

# Convert list to string for simple text searching
forecastString = str(forecast)

# Initialise rain check variable
RainOracle = "It will not rain."

# Search for synonyms of rain
if forecastString.find("storm") > 0:
    RainOracle = "It will rain."
if forecastString.find("Storm") > 0:
    RainOracle = "It will rain."
if forecastString.find("Thunder") > 0:
    RainOracle = "It will rain."
if forecastString.find("Shower") > 0:
    RainOracle = "It will rain."
if forecastString.find("Rain") > 0:
    RainOracle = "It will rain."
if forecastString.find("Snow") > 0:
    RainOracle = "It will rain."

print("Rain Oracle says:", RainOracle)
