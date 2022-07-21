import requests
import json

def getMetadatakey (item):
    api_url = "http://169.254.169.254/latest/meta-data/"+item
    data = requests.get(api_url)
    return data

item = 'InstanceId'
mdata = getMetadatakey(item)
print(mdata)