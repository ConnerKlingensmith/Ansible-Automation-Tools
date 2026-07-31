from netmiko import ConnectHandler

device = {
        "device_type": "cisco_ios",
        "host": "10.0.1.29",
        "username": "ansible",
        "password": "Cisco123!",
}

connection = ConnectHandler(**device)
output = connection.send_command("show version")
print(output)
connection.disconnect()
