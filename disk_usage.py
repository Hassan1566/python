#!/usr/bin/env python3
import os
import psutil
import sys

def check_reboot():
    """Check if a reboot is required."""    
    return os.path.exists('/run/reboot-required') or os.path.exists('/var/run/reboot-required')

def check_disk_usage(disk, min_gb, min_percentage):
    """Check if there is enough free disk space."""
    disk_usage = psutil.disk_usage(disk)
    min_bytes = min_gb * 1024 * 1024 * 1024
    if disk_usage.free < min_bytes or disk_usage.percent > (100 - min_percentage):
        return False
    return True

def check_root_full():
    """Check if the root partition is full."""
    return check_disk_usage("C://", 2, 10)

def main():
    if check_reboot():
        print("Reboot is required.")
        sys.exit(1)

    if not check_root_full():
        print("Root partition is full.")
        sys.exit(1)
    
    print("Everything is within the acceptable range.")
    sys.exit(0)

main()