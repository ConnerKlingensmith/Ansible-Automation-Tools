from netmiko import ConnectHandler

device = {
        "device_type": "cisco_ios",
        "host": "10.0.1.29",
        "username": "ansible",
        "password": "Cisco123!",
}

config_commands = [
        "interface Loopback1",
        "description Pushed by Netmiko",
        "ip address 172.16.10.1 255.255.255.255",
]

connection = ConnectHandler(**device)

output = connection.send_config_set(config_commands)
print(output)

connection.save_config()
print("--- saved to startup-config ---")

print(connection.send_command("show running-config interface Loopback1"))
connection.disconnect()

"""
send_config_set(list)	                    -->  Enters config mode, sends each line, exits config mode
save_config()	                            -->  Runs write memory so the change survives a reload or an EC2 stop/start
show running-config interface Loopback1	    -->  Verifies from the device, not from your assumptions
"""
