#!/bin/bash
meeting_info=$(zenity --forms --text "Add reminder information" --add-entry "Meeting Title" --add-entry "Meeting Date" --add-entry "Emails")

if [[ -n "$meeting_info" ]]; then
  python3 send_reminder.py "$meeting_info"
else
  echo -e "\nError: Zenity failed to launch or nothing was entered!"
  echo "Because you are using WSL (Kali Linux), Zenity requires an X-server like WSLg or VcXsrv to display the popup."
fi