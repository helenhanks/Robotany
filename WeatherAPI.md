[Return to Readme](README.md)

# Query a Weather Service
You can access the API of the weather.gov service to see if it is going to rain later in the day. 
Although I developed the script to do this, I actually found the weather forecast so unreliable I now prefer to check my water barrrel level to see if it rained overnight.

## Parts

No hardware required apart from Raspberry Pi.

## Important Steps

### Figure out your gridpoints
Before crafting your query, you need to determine the coordinates of where your project is going to be based and figure out which weather.gov grids these correspont to.

1. Look up your GPS coordinates (latitude and longitude) using any online tool (e.g. https://www.latlong.net/)
2. Naviate to `https://api.weather.gov/points/{latitude},{longitude}` to find out your weather.gov grids
3. When the JSON text comes back, look for the fields that say `gridX` and `gridY`. The numbers in here are your grids

### Find your endpoint

Your endpoint is `https://api.weather.gov/gridpoints/HGX/{gridX},{gridY}/forecast/hourly`, with the values for your `gridX` and `gridY` substituted in. 
If you navigate to this address in a browser, you will be able to look at the JSON data returned.

### Run your query
The script required to run the query is stored in `code/weatherAPI.py`. Just substitute in your own grid numbers.

[Return to Readme](README.md)
