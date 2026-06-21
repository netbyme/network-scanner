# network-scanner
# Scans a network range and detects which devices are alive
# Uses ping to check each IP and saves results to a report

import subprocess
import ipaddress

def ping_ip(ip):
    # ping once with 1 second timeout
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1", str(ip)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    # returns True if device responded
    return result.returncode == 0

def scan_network(network_range):
    print(f"Scanning {network_range}...")
    
    alive = []
    dead = []
    
    # loop through every IP in the range
    for ip in ipaddress.IPv4Network(network_range, strict=False):
        if ping_ip(ip):
            print(f"[UP]   {ip}")
            alive.append(str(ip))
        else:
            print(f"[DOWN] {ip}")
            dead.append(str(ip))
    
    return alive, dead

# scan this range
alive, dead = scan_network("192.168.1.0/24")

print(f"\nTotal UP: {len(alive)}")
print(f"Total DOWN: {len(dead)}")