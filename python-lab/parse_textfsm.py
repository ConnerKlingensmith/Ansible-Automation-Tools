# Adding use_textfsm=True tells Netmiko to run the matching template and return a list of dictionaries instead of raw text.

from netmiko import ConnectHandler

device = {
        "device_type": "cisco_ios",
        "host": "10.0.1.29",
        "username": "ansible",
        "password": "Cisco123!",
}

connection = ConnectHandler(**device)
interfaces = connection.send_command("show ip interface brief", use_textfsm=True)
connection.disconnect()

print(type(interfaces))
for row in interfaces:
    print(f"{row['interface']:25} {row['ip_address']:16} {row['status']}")  # :25 / :16 adds whitespace between rows in output
