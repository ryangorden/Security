import requests
from requests.auth import HTTPBasicAuth
from jinja2 import Environment, FileSystemLoader
from yaml import safe_load

# opening up variable file
with open("pre_web_auth.yml", 'r') as file:
    var=safe_load(file)


# combining variable file with template file
# this is how will build our payload data
env= Environment(loader=FileSystemLoader("."))
template= env.get_template("template.j2")
payload= template.render(var)

# uncomment the line below for payload validation
# print(payload)

#creating url to ise
base_server= "https://10.10.20.70:9060"
dacl_endpoint="/ers/config/authorizationprofile/"
url= f"{base_server}{dacl_endpoint}"

headers= {
          "Accept": "application/json",
          "Content-Type": "application/json"
}

auth= HTTPBasicAuth("admin","C1sco12345!")

# sending post request to ise
resp= requests.post(url, headers=headers,auth=auth, data=payload,verify=False)
print(resp.status_code)
print(resp.text)
