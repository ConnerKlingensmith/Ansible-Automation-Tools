from netmiko import ConnectHandler

USER = "ansible"
PASSWORD = "Cisco123!"

devices = [
        {"device_type": "cisco_ios", "host": "10.0.1.29", "username": USER, "password": PASSWORD},
        {"device_type": "cisco_ios", "host": "10.0.1.19", "username": USER, "password": PASSWORD},
]

commands = ["show ip interface brief", "show ip route"]

for device in devices:
    connection = ConnectHandler(**device)
    hostname = connection.find_prompt().strip("#>")
    print(f"\n===== {hostname} ({device['host']}) =====")
    for command in commands:
        print(f"\n--- command ---")
        print(connection.send_command(command))
    connection.disconnect()
