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
    min_gb = min_gb * 1024 * 1024 * 1024 
    if disk_usage.free < min_gb or disk_usage.percent > (100 - min_percentage):
        return False
    return True


def main():
    if check_reboot():
        print("Reboot is required.")
        sys.exit(1)

    if not check_disk_usage('C:\\', 2, 10):
        print("Disk usage is above the threshold.")
        sys.exit(1)
    
    print("Everything is within the acceptable range.")
    sys.exit(0)