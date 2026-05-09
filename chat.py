# Simple Chat Application

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def __str__(self):
        return f"[{self.sender.username}]: {self.content}"

class ChatRoom:
    def __init__(self):
        self.messages = []      
        self.active_users = []  

    def join_room(self, user):
        if user not in self.active_users:
            self.active_users.append(user)
            print(f"--- {user.username} has entered the chat ---")
        else:
            print(f"{user.username} is already in the room.")

    def leave_room(self, user):
        if user in self.active_users:
            self.active_users.remove(user)
            print(f"--- {user.username} has left the chat ---")
        else:
            print(f"{user.username} is not in the room.")

    def send_message(self, user, content):
        if user in self.active_users:
            new_message = Message(user, content)
            self.messages.append(new_message)
        else:
            print(f"Error: {user.username} must join the room before sending a message.")

    def view_chat_history(self):
        print("\n--- Chat History ---")
        if not self.messages:
            print("No messages yet.")
        else:
            for msg in self.messages:
                print(msg)
        print("--------------------\n")



# 1. Create Users
user1 = User("Alice", "pass123")
user2 = User("Bob", "secure456")

# 2. Initialize ChatRoom
general_chat = ChatRoom()

# 3. Users joining and interacting
general_chat.join_room(user1)
general_chat.join_room(user2)

general_chat.send_message(user1, "Hey everyone!")
general_chat.send_message(user2, "Hello Alice, how's it going?")
general_chat.send_message(user1, "Doing great, just coding!")

# 4. A user leaves
general_chat.leave_room(user2)

# 5. View History
general_chat.view_chat_history()