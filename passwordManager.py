class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, website, username, password):
        if website in self.passwords:
            self.passwords[website][username] = password
        else:
            self.passwords[website] = {username: password}

    def get_password(self, website, username):
        if website in self.passwords and username in self.passwords[website]:
            return self.passwords[website][username]
        else:
            return None

    def list_websites(self):
        return list(self.passwords.keys())


# Example Usage:
password_manager = PasswordManager()

# Add passwords
password_manager.add_password("example.com", "user1", "strong_password1")
password_manager.add_password("example.com", "user2", "strong_password2")
password_manager.add_password("another-site.com", "user1", "secure_pass")

# Get passwords
password1 = password_manager.get_password("example.com", "user1")
print("Password for user1 on example.com:", password1)

password2 = password_manager.get_password("another-site.com", "user1")
print("Password for user1 on another-site.com:", password2)

# List websites
websites = password_manager.list_websites()
print("Websites:", websites)


