import requests
import json
import base64

url = "https://10.1.1.1/mgmt/shared/appsvcs/declare"



with open("creds.txt", "r") as f:
    creds = base64.b64encode(bytes(f.read().strip(), 'utf-8')) # bytes
    auth = creds.decode('utf-8') # convert bytes to string
    basic_auth = f"Basic {auth}"

with open("https_app.json", "r") as f:
    payload = json.load(f)

headers = {
  'Content-Type': 'application/json',
  'Authorization': basic_auth,

}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload), verify= False)

print(response.status_code)
