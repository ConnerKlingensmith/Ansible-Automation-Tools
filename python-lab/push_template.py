from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler

USER = "ansible"
PASSWORD = "Cisco123!"

devices = [
    {"host": "10.0.1.29", "loopback_ip": "172.16.10.1", "description": "Site A loopback"},
    {"host": "10.0.1.19", "loopback_ip": "172.16.10.2", "description": "Site B loopback"},
]

env = Environment(loader=FileSystemLoader("."), trim_blocks=True, lstrip_blocks=True)
template = env.get_template("loopback.j2")

for entry in devices:
    config = template.render(**entry)

    print(f"\n===== {entry['host']} =====")
    print(config)

    connection = ConnectHandler(
            device_type="cisco_ios",
            host=entry['host'],
            username=USER,
            password=PASSWORD,
    )

    output = connection.send_config_set(config.splitlines())

    if "Invalid input" in output or "Incomplete command" in output:
        print("!! the device rejected part of this config:")
        print(output)
    else:
        connection.save_config()
        print(connection.send_command("show running-config interface Loopback1"))

    connection.disconnect()

"""
FileSystemLoader(".")	        -->  Looks for templates in the current directory
template.render(**entry)	    -->  Substitutes {{ }} variables with this device's values
config.splitlines()	            -->  Turns the rendered text block into the list send_config_set expects
Checking the output	            -->  Catches a rejected line before you report success
"""
