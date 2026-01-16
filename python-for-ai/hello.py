print("Hello, World!")
print("I am learning Python for AI.")

import requests

# Download a webpage
response = requests.get("https://api.github.com")
print(response.status_code)