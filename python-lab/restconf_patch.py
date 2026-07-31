import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = "10.0.1.29"
AUTH = ("apiuser", "L@bRestconf123")
HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

url = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces/interface=Loopback0"

payload = {
    "ietf-interfaces:interface": [
        {
            "name": "Loopback0",
            "description": "Configured via RESTCONF",
        }
    ]
}

response = requests.patch(url, auth=AUTH, headers=HEADERS, json=payload, verify=False)
print("Status code:", response.status_code)     # 204 means success, no content
if response.status_code >= 400:
    print(response.text)
