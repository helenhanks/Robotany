[Return to Readme](README.md)
## Using Samsung SmartThings to Control your Smart Devices via API
Samsung SmartThings is a service that lets you add most home smart devices to its interface. Once you have done that, you can control or look at those devices through its web portal or phone app. However, they also let you set up APIs for your devices so you can send commands via HTML. This means you can control them from your Raspberry Pi or any other computer using a script or the command line.

## Set up Smart Things Account and Develop APP
1. Go to https://account.smartthings.com/
2. Set up an account
3. Add smart device and set up location

## Creating a Webapp and API
Once you have set up a "device" in a "location", you can create a webapp with an API by following the tutorial here: https://docs.smartthings.com/en/latest/smartapp-web-services-developers-guide/tutorial-part1.html

A few hints:
* Enable OAuth
* The redirect URI can be literally any website you want. I think this is possibly a bug but I'm going to exploit it rather than build my own website and server just for this!
* The webapp can be tested in a simulator. It gives you a token and an endpoint to play with. This is great for testing but it disappears as soon as you navigate away from the page. To get permanent access to your app you need to go through OAuth.

## Using OAuth to Generate a Token and Endpoint
OAuth is a series of steps you have to go through to generate a token and find out your endpoint. Basically it goes like this:

1. Navigate to a speciic URL with your client ID and redirect URI in the headers and request a code by logging into SmartThings and authorising access to the app.
2. Use the code to go to another URL and request an access token
3. Use this access token to go to yet another URL to request an endpoint
4. Use the token and endpoint to build your command to switch your devices on and off

I have written a script that automates nearly all of this. The only manuel bit is the first step which must be done in a web browser. The script is in `code/SmartThingsOAuth.py`.

### Useful Links
#### Smart Things API Documentation
https://docs.smartthings.com/en/latest/
#### Tutorial on Creating API Endpoint
https://docs.smartthings.com/en/latest/smartapp-web-services-developers-guide/tutorial-part1.html
#### Utility to convert from curl to python
https://curl.trillworks.com/

## Command line code
#### Turn on
`curl -H "Authorization: Bearer _api-token_" -X PUT "_api-endpoint_/switches/on"`

#### Turn off
`curl -H "Authorization: Bearer _api-token_" -X PUT "_api-endpoint_/switches/off"`
  
## Python Code 

#### Turn on
`import requests

headers = {'Authorization': 'Bearer <api token>',}

response = requests.put('https://graph-na04-useast2.api.smartthings.com/api/smartapps/installations/_api-endpoint_/switches/on', headers=headers)`
  
#### Turn Off
`import requests

headers = {'Authorization': 'Bearer _api-token_',}

response = requests.put('https://graph-na04-useast2.api.smartthings.com/api/smartapps/installations/_api-endpoint_/switches/off', headers=headers)`

[Return to Readme](README.md)
