import sys

def main():
    # Ensure the script received the expected argument from the bash script
    if len(sys.argv) < 2:
        print("Error: Missing meeting info.")
        print("Usage: python3 send_reminder.py 'Title|Date|Emails'")
        sys.exit(1)

    meeting_info = sys.argv[1]
    
    # Parse the string based on Zenity's default pipe '|' separator
    try:
        title, date, emails = meeting_info.split('|')
    except ValueError:
        print("Error: Input does not match the expected format 'Title|Date|Emails'.")
        sys.exit(1)
        
    # Create a simple reminder message
    message = (
        f"=========================================\n"
        f"              MEETING REMINDER           \n"
        f"=========================================\n"
        f"📌 Title:     {title}\n"
        f"📅 Date:      {date}\n"
        f"✉️  Attendees: {emails}\n"
        f"========================================="
    )

    # Print the simple reminder message to the console
    print(message)

if __name__ == "__main__":
    main()
