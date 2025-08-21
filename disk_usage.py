#!/usr/bin/env python3
import os
import psutil
import sys
import socket
def check_reboot():
    """Check if a reboot is required."""    
    return os.path.exists('/run/reboot-required') or os.path.exists('/var/run/reboot-required')

def check_disk_usage(disk, min_gb, min_percentage):
    """Check if there is enough free disk space."""
    disk_usage = psutil.disk_usage(disk)
    min_bytes = min_gb * 1024 * 1024 * 1024
    if disk_usage.free < min_bytes or disk_usage.percent > (100 - min_percentage):
        return True
    return False

def check_root_full():
    """Check if the root partition is full."""
    return check_disk_usage("C://", 2, 10)

def check_no_network():
    """Check if there is no network connectivity."""
    try:
        socket.create_connection(("www.google.com", 80))
        return False
    except:
        return True

def main():
    check = [
        (check_reboot, "Reboot is required"),
        (check_root_full, "Root partition is full."),
        (check_no_network, "No network connectivity.")
    ]
    every_check = True
    for func, msg in check:
        if func():
            print(msg)
            every_check = False
    if every_check:
        print("Everything is within the acceptable range.")
    sys.exit(1)

    print("Everything is good.")
    sys.exit(0)

main()