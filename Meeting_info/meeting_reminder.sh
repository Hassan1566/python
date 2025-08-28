#!/bin/bash
meeting_info=$(Zenity --forms --text "Add reminder information" --add-entry "Meeting Title" --add-entry "Meeting Date" --add-entry "Emails" 2>/dev/null)

if [[ -n "$meeting_info" ]]; then
  python3 send_reminder.py "$meeting_info"
fi