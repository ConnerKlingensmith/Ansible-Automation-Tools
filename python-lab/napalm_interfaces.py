# Retrieve interface details and save them to json

import json
from napalm import get_network_driver

driver = get_network_driver("ios")

device = driver(hostname="10.0.1.29", username="ansible", password="Cisco123!")
device.open()
interfaces = device.get_interfaces()
device.close()

# Show a structured summary
for name, data in interfaces.items():
    state = "up" if data["is_up"] else "down"
    print(f"{name:25} {state:5} {data['description']}")

# Save the full structure as a JSON for reuse
with open("c8kv-1_interfaces.json", "w") as f:
    json.dump(interfaces, f, indent=2)
print("\nSaved c8kv-1_interfaces.json")
