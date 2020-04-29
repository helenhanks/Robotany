### Useful Links
#### Smart Things API Documentation
https://docs.smartthings.com/en/latest/
#### Tutorial on Creating API Endpoint
https://docs.smartthings.com/en/latest/smartapp-web-services-developers-guide/tutorial-part1.html
#### Utility to convert from curl to python
https://curl.trillworks.com/

##Set up SMart Things Account and Develop APP
https://account.smartthings.com/

## Command line code
#### Turn on
curl -H "Authorization: Bearer <api token>" -X PUT "<api endpoint>/switches/on"

#### Turn off
curl -H "Authorization: Bearer <api token>" -X PUT "<api endpoint>/switches/off"
  
## Python Code
#### Turn on
import requests

headers = {
    'Authorization': 'Bearer <api token>',
}

response = requests.put('https://graph-na04-useast2.api.smartthings.com/api/smartapps/installations/<api endpoint>/switches/on', headers=headers)
  
#### Turn Off
import requests

headers = {
    'Authorization': 'Bearer <api token>',
}

response = requests.put('https://graph-na04-useast2.api.smartthings.com/api/smartapps/installations/<api endpoint>/switches/off', headers=headers)
