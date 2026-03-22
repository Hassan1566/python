#!/bin/bash
# This is a purely text-based terminal script alternative to use on WSL without a GUI

echo "=== Add reminder information ==="

# Prompt the user for information right in the terminal
read -p "Meeting Title: " title
read -p "Meeting Date: " date
read -p "Emails: " emails

# Check if at least the title was provided
if [[ -n "$title" ]]; then
  # Format it using the exact same pipe '|' separator the python script expects
  meeting_info="$title|$date|$emails"
  
  echo -e "\nRunning Python script..."
  python3 send_reminder.py "$meeting_info"
else
  echo "Error: Meeting title is specifically required. Exiting."
fi
