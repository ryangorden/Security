import requests
from requests.auth import HTTPBasicAuth
import json
from pprint import pprint


#gathering  server root url, credentials, and header
#infomation to form url requests.
server= "https://example.com"
auth = HTTPBasicAuth(username,password)
headers = {"Accept": "application/json"}


def get_users(server,auth,headers):
    port =9060
    internal_users_endpoint = "/ers/config/internaluser"
    url= f"{server}:{port}{internal_users_endpoint}"
    resp = requests.get(url, auth=auth, headers=headers)
    return json.loads(resp.text)


if __name__ == "__main__":
    users= get_users(server,auth,headers)
    pprint(users)
