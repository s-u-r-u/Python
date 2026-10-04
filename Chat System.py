class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        return f"Username: {self.username}, Email: {self.email}"
class Message:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content

    def display_message(self):
        return f"From: {self.sender.username}, To: {self.recipient.username}, Message: {self.content}"
class Chatroom:
    def __init__(self):
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, sender, recipient, content):
        message = Message(sender, recipient, content)
        self.messages.append(message)

    def display_messages(self):
        return [message.display_message() for message in self.messages]
