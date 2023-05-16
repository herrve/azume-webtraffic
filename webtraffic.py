import requests
import time

# Define the list of websites to visit.
websites = ["https://www.google.com", "https://www.yahoo.com", "https://www.bing.com"]

# Start the traffic generator.
while True:
    # Select a random website from the list.
    website = websites[random.randint(0, len(websites) - 1)]

    # Make a request to the website.
    response = requests.get(website)

    # Wait for a random amount of time before making the next request.
    time.sleep(random.randint(1, 5))