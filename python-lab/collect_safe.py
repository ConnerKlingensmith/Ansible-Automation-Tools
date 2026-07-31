# File Saving and Error Handling -- One failure DOESN'T STOP the whole run

from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

USER = "ansible"
PASSWORD = "Cisco123!"

devices = [
    {"device_type": "cisco_ios", "host": "10.0.1.250", "username": USER, "password": PASSWORD},   # Wrong IP -- will output Exception but still run on other router
    {"device_type": "cisco_ios", "host": "10.0.1.19", "username": USER, "password": PASSWORD},
]

for device in devices:
    host = device['host']
    try:
        connection = ConnectHandler(**device)
        hostname = connection.find_prompt().strip("#>")
        output = connection.send_command("show ip interface brief")
        connection.disconnect()

        with open(f"{hostname}_interfaces.txt", "w") as f:
            f.write(output)
        print(f"{host}: collected and saved as {hostname}_interfaces.txt")

    except NetmikoTimeoutException:
        print(f"{host}: TIMEOUT - is the router booted and reachable?")
    except NetmikoAuthenticationException:
        print(f"{host}: AUTH FAILED - check the username/password")

# When Ran, will create two files showing the Interfaces of each router
