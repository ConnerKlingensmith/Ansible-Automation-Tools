import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = "10.0.1.29"
AUTH = ("apiuser", "L@bRestconf123")
HEADERS = {"Accept": "application/yang-data+json"}

url = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces/interface=Loopback0"

response = requests.get(url, auth=AUTH, headers=HEADERS, verify=False)

print("Status code:", response.status_code)
print(response.json())

"""
https://.../restconf/data/...        -->  The RESTCONF URL identifying a resource
interface=Loopback0	                 -->  Selects one specific interface
Accept: application/yang-data+json	 -->  Ask the device to reply in JSON
auth=(user, pass)	                 -->  HTTPS basic authentication from creds RESTCONF configured on router
verify=False	                     -->  Accept the device's self-signed certificate
status 200	                         -->  The request succeeded
"""
