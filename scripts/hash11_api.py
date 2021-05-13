import requests
import json


hash11_api = "https://api.hashdex.io/prod/marketdata/v1/inav/HASH11"

response = requests.get(hash11_api) # 202 if working


#print(response)
print(response.status_code)
print()
#print(response.json())


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#jprint(response.json())
print()

info = response.json()['info']
currency = response.json()['currency']
inavpershare = response.json()['inavPerShare']
#jprint(info)

jprint(inavpershare)