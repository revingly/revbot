import json
global token

json_file = 'config/creds.json'

def readCredentials():
    with open(json_file, 'r') as creds:
        data = json.load(creds)
        return data

def writeCredentials(data):
    with open(json_file, 'w') as creds:
        json.dump(data, creds)

data = readCredentials()
token = data['TOKEN']
if token:
    readCredentials()
