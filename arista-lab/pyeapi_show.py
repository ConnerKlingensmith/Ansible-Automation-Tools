import pyeapi

node = pyeapi.connect_to("leaf1")

result = node.enable("show ip interface brief")
interfaces = result[0]["result"]["interfaces"]

for name, data in interfaces.items():
    addr = data["interfaceAddress"]["ipAddr"]["address"]
    print(f"{name:20} {addr}")
