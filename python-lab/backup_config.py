from datetime import datetime
from pathlib import Path

from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

USER = "ansible"
PASSWORD = "Cisco123!"

devices = [
        {"device_type": "cisco_ios", "host": "10.0.1.29", "username": USER, "password": PASSWORD},
        {"device_type": "cisco_ios", "host": "10.0.1.19", "username": USER, "password": PASSWORD},
]

BACKUP_DIR = Path("backups")
BACKUP_DIR.mkdir(exist_ok=True)
stamp = datetime.now().strftime("%Y%m%d-%H%M%S")

for device in devices:
    host = device['host']
    try:
        connection = ConnectHandler(**device)
        hostname = connection.find_prompt().strip("#>")
        running = connection.send_command("show running-config", read_timeout=90)
        connection.disconnect()

        path = BACKUP_DIR / f"{hostname}-{stamp}.cfg"
        path.write_text(running)
        print(f"{host}: saved {path} ({len(running.splitlines())} lines)")

    except NetmikoTimeoutException:
        print(f"{host}: TIMEOUT - is the router booted and reachable?")
    except NetmikoAuthenticationException:
        print(f"{host}: AUTH FAILED - check the username/password")

"""
read_timeout=90	                    -->  show running-config is long — give Netmiko time to read it all
find_prompt().strip("#>")	        -->  Uses the device's own hostname for the filename
BACKUP_DIR.mkdir(exist_ok=True)	    -->  Creates backups/ once, silently, if it isn't there
datetime.now().strftime(...)	    -->  One timestamp for the whole run, so a set of backups sorts together
"""
