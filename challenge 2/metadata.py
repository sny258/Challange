import requests
import json

def getMetadata ():
    api_url = "http://169.254.169.254/latest/meta-data/"
    response = requests.get(api_url)
    data = json.loads(response)
    return data

mdata = getMetadata()
print(mdata)