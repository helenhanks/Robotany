[Return to Readme](README.md)

### Useful Links
#### Smart Things API Documentation
https://docs.smartthings.com/en/latest/
#### Tutorial on Creating API Endpoint
https://docs.smartthings.com/en/latest/smartapp-web-services-developers-guide/tutorial-part1.html
#### Utility to convert from curl to python
https://curl.trillworks.com/

##Set up Smart Things Account and Develop APP
1. Go to https://account.smartthings.com/
2. Set up an account
3. Add smart device and set up location
4. Go to My Smart Apps and make a web app
5. Use endpoint, token, oath etc to send commands from whatever script to your new app's API

## Command line code
#### Turn on
curl -H "Authorization: Bearer _api-token_" -X PUT "_api-endpoint_/switches/on"

#### Turn off
curl -H "Authorization: Bearer _api-token_" -X PUT "_api-endpoint_/switches/off"
  
## Python Code 
(note: Markdown messes up the formating, check raw code)
#### Turn on
import requests

headers = {
    'Authorization': 'Bearer <api token>',
}

response = requests.put('https://graph-na04-useast2.api.smartthings.com/api/smartapps/installations/_api-endpoint_/switches/on', headers=headers)
  
#### Turn Off
import requests

headers = {
    'Authorization': 'Bearer _api-token_',
}

response = requests.put('https://graph-na04-useast2.api.smartthings.com/api/smartapps/installations/_api-endpoint_/switches/off', headers=headers)

[Return to Readme](README.md)
