import requests
import json

# SmartThings App Credentials from your account
import SmartThingsCredentials as credentials

# Authorization workflow documented here: https://docs.smartthings.com/en/latest/smartapp-web-services-developers-guide/authorization.html

## GET CODE
#GET https://graph.api.smartthings.com/oauth/authorize?
#        response_type=code&
#        client_id=YOUR-SMARTAPP-CLIENT-ID&
#        scope=app&
#        redirect_uri=YOUR-SERVER-URI

UrlString = 'https://graph.api.smartthings.com/oauth/authorize?response_type=code&client_id='+ credentials.ClientID + '&scope=app&redirect_uri=' + credentials.RedirectURI
print('1. To begin the OAuth process, navigate in a web browser to: ' + UrlString)
print('2. Sign into your SmartThings Account and select the app/switch.')
print('3. When you are finally redirected to your redirect URI, extract the code from the browser address bar.')
code = input('Enter code: ')
print('Code entered is ' + code)

## GET ACCESS TOKEN
#POST https://graph.api.smartthings.com/oauth/token HTTP/1.1
#Host: graph.api.smartthings.com
#Content-Type: application/x-www-form-urlencoded
#grant_type=authorization_code&code=YOUR_CODE&client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&redirect_uri=YOUR_REDIRECT_URI

TokenQueryHeaders = {
    'Host': 'graph.api.smartthings.com',
    'Content-Type' : 'application/x-www-form-urlencoded',
}

TokenQueryString = 'https://graph.api.smartthings.com/oauth/token?grant_type=authorization_code&code=' + code + '&client_id=' + credentials.ClientID + '&client_secret=' + credentials.ClientSecret + '&redirect_uri=' + credentials.RedirectURI                         
TokenQueryResponse = requests.post(TokenQueryString, headers = TokenQueryHeaders)
                         
#print(TokenQueryResponse.text)
#token = input('Copy and paste "access_token" value from above: ')

token = json.loads(TokenQueryResponse.text)["access_token"]
print('Your token is ' + token)

## GET ENDPOINT
#GET -H "Authorization: Bearer ACCESS-TOKEN" "https://graph.api.smartthings.com/api/smartapps/endpoints"

EndpointQueryHeaders = {'Authorization': 'Bearer ' + token,}
EndpointQueryResponse = requests.get('https://graph.api.smartthings.com/api/smartapps/endpoints', headers = EndpointQueryHeaders)

#print(EndpointQueryResponse.text)
#endpoint = input('Copy and paste "uri" value from above: ')

endpoint = json.loads(EndpointQueryResponse.text)[0]["uri"]
print('Your endpoint is ' + endpoint)

# PRINT DETAILS ON HOW TO MAKE REST CALLS
print('To make a REST call in the command line use: ')
print('curl -H "Authorization: Bearer ' + token + '" -X PUT "' + endpoint + '/switches/on"')
print('Happy coding!')

## MAKE A REST CALL TO TEST SMART SWITCH
headers = {'Authorization': 'Bearer ' + token,}
while True:
    command = ''
    command = input('Turn switch on or off? Type "on" or "off" to activate switch. Press enter to skip. ')
    if command == 'on':
        response = requests.put(endpoint + '/switches/on', headers=headers)
    elif command == 'off':
        response = requests.put(endpoint + '/switches/off', headers=headers)
    elif command == '':
        exit()


