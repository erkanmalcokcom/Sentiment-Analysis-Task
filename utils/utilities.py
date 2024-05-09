import os

class Screen:
    def __init__(self):
        pass

    def create_banner_and_message(self, message):
        # Get the size of the terminal window
        rows, columns = os.popen('stty size', 'r').read().split()
        columns = int(columns)

        # Create a banner with the welcome message
        banner = "*" * columns
        centered_message = message.center(columns - len(message) // 2)

        return banner, centered_message

    def welcome_screen(self):
        welcome_message = "TEXT SENTIMENT ANALYSIS"
        banner, centered_message = self.create_banner_and_message(welcome_message)

        # Print the banner and centered message with an emoji (optional)
        print(banner)
        print(centered_message, chr(128516))  # Smiling face emoji
        print(banner + "\n")
