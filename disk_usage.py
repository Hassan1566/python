#!/usr/bin/env python3

import psutil
import sys

def check_disk_usage(disk, min_absolute, min_percentage):
    """Check if there is enough free disk space."""
    disk_usage = psutil.disk_usage(disk)
    if disk_usage.free < min_absolute or disk_usage.percent > (100 - min_percentage):
        return False
    return True

# Example: 2 GB minimum free, 10% minimum free percentage
min_absolute = 2 * 1024 * 1024 * 1024  # 2 GB
min_percentage = 10

if not check_disk_usage('C:\\', min_absolute, min_percentage):
    print("Disk usage is above the threshold.")
    sys.exit(1)
else:
    print("Disk usage is within the acceptable range.")
    sys.exit(0)