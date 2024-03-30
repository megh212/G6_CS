import time
import ipaddress
import subprocess

def change_ip(interface, new_ip):
    try:
        # Convert IP address to IPv4Address object
        ip_address = ipaddress.IPv4Address(new_ip)
        # Execute netsh command to change IP address
        subprocess.run(["netsh", "interface", "ip", "set", "address", f"name={interface}", f"source=static", f"addr={ip_address}", "mask=255.255.255.0"])
        return True
    except ValueError:
        return False

# Example usage:
interface = 'Wi-Fi'  
ip_file = 'ip-list.txt'

# Read IP addresses from the file
with open(ip_file, 'r') as file:
    ip_addresses = file.readlines()
ip_addresses = [ip.strip() for ip in ip_addresses]

while True:
    for new_ip in ip_addresses:
        if change_ip(interface, new_ip):
            print(f"IP address of {interface} changed to {new_ip}.")
            time.sleep(20)
        else:
            print("Failed to change IP address.")
