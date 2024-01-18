import hashlib
import base64

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, original_url):
        # Generate a unique identifier for the URL using SHA-256 hash
        url_hash = hashlib.sha256(original_url.encode()).digest()
        # Encode the hash to base64 to create a short identifier
        short_identifier = base64.urlsafe_b64encode(url_hash)[:8].decode()

        # Map the short identifier to the original URL
        self.url_mapping[short_identifier] = original_url

        # Construct the shortened URL
        shortened_url = f"http://short.url/{short_identifier}"
        return shortened_url

    def retrieve_url(self, short_identifier):
        # Retrieve the original URL using the short identifier
        original_url = self.url_mapping.get(short_identifier)
        return original_url

# Example Usage:
url_shortener = URLShortener()

original_url = "https://www.example.com"
shortened_url = url_shortener.shorten_url(original_url)

print(f"Original URL: {original_url}")
print(f"Shortened URL: {shortened_url}")

# Retrieving the original URL
retrieved_url = url_shortener.retrieve_url(shortened_url.split("/")[-1])
print(f"Retrieved URL: {retrieved_url}")