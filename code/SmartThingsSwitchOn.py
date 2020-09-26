import requests

# Read in SmartThings token and endpoint from separate file
import SmartThingsCredentials as credentials

# Define headers
headers = {
    'Authorization': 'Bearer ' + credentials.token,
}

# Build on command
response = requests.put(credentials.endpoint + '/switches/on', headers=headers)
