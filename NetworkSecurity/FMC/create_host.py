import requests
from requests.auth import HTTPBasicAuth
import json

server = "https://example.com"
headers = {"Content-Type": "application/json", "Accept": "application/json"}
auth = HTTPBasicAuth(username, password)

def get_token(server, auth, headers):
    token_endpoint = "/api/fmc_platform/v1/auth/generatetoken"
    url = f"{server}{token_endpoint}"
    print("getting token")
    resp = requests.post(url, auth = auth, headers = headers, verify = False)
    token = resp.headers["X-auth-access-token"]
    headers["X-auth-access-token"] = token
    print(headers)
    return headers



def create_host(server,token, payload):
    host_endpoint = "/api/fmc_config/v1/domain/<domain UUID>/object/hosts"
    url = f"{server}{host_endpoint}"
    print(url)
    headers = token
    print("creating object")
    print(headers)
    resp = requests.post(url, headers = headers,data = json.dumps(payload), verify = False)
    print("object created")

    print(json.loads(resp.text))

def delete_host(token):
    url = input("Enter uri: ")
    headers = token
    resp = requests.delete(url, headers=headers, verify=False)
    return resp.status_code


if __name__ == "__main__":
    token = get_token(server, auth, headers)
    payload = {"name": "a-10.120.16.233",
               "description": "Create via api",
               "value": "10.120.16.233",
               "type": "Host"}
    host = create_host(server,token, payload)
    remove_hosts = delete_host(token)
    print(remove_hosts)
