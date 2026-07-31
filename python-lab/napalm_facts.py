import json
from napalm import get_network_driver

driver = get_network_driver("ios")

hosts = ["10.0.1.29", "10.0.1.19"]

for host in hosts:
    device = driver(hostname=host, username="ansible", password="Cisco123!")
    device.open()
    facts = device.get_facts()
    device.close()

    print(f"\n===== {facts['hostname']} =====")
    print(f"  Model:      {facts['model']}")
    print(f"  Version:    {facts['os_version'].split(',')[0]}")
    print(f"  Serial:     {facts['serial_number']}")
    print(f"  Uptime:     {facts['uptime']} seconds")
    print(f"  Interfaces: {facts['interface_list']}")
    
