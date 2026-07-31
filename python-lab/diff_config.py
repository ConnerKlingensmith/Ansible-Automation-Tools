import difflib
from pathlib import Path

from netmiko import ConnectHandler

NOISE = (
        "Building configuration",
        "Current configuration",
        "! Last configuration change",
        "! NVRAM config last update",
)

def clean(text):
    """Drop blank lines and the lines that change on every capture."""
    return [
            line.strip()
            for line in text.splitlines()
            if line.strip() and not line.startswith(NOISE)
    ]

device = {
    "device_type": "cisco_ios",
    "host": "10.0.1.29",
    "username": "ansible",
    "password": "Cisco123!",
}

connection = ConnectHandler(**device)
hostname = connection.find_prompt().strip("#>")
current = connection.send_command("show running-config", read_timeout=90)
connection.disconnect()

backups = sorted(Path("backups").glob(f"{hostname}-*.cfg"))
if not backups:
    raise SystemExit(f"No backup found for {hostname} - run backup_configs.py first")

baseline = backups[0]
print(f"Comparing {baseline} with the running config on {hostname}\n")

diff = difflib.unified_diff(
        clean(baseline.read_text()),
        clean(current),
        fromfile=str(baseline),
        tofile=f"{hostname} (now)",
        lineterm=""
)

changes = list(diff)
if changes:
    for line in changes:
        print(line)

else:
    print("No differences.")
