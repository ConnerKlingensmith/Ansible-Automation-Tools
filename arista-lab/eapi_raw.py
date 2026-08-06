import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SWITCH = "leaf1"
AUTH = ("arista", "Arista123!")

payload = {
        "jsonrpc": "2.0",
        "method": "runCmds",
        "params": {
            "version": 1,
            "cmds": ["show version"],
            "format": "json",
        },
        "id": "lab14",
}

url = f"https://{SWITCH}/command-api"
response = requests.post(url, json=payload, auth=AUTH, verify=False)

result = response.json()["result"][0]
print("Model: ", result["modelName"])
print("Version: ", result["version"])
print("Serial: ", result["serialNumber"])
