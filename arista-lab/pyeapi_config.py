# This scripts Pushes a CONFIG Change

import pyeapi

node = pyeapi.connect_to("leaf1")

node.config([
    "interface Loopback14",
    "description Configured via pyeapi",
    "ip address 10.14.14.14/32",
])
print("Loopback14 configured")

# Confirm the change
result = node.enable("show interfaces Loopback14")
desc = result[0]["result"]["interfaces"]["Loopback14"]["description"]
print("Description is now:", desc)
