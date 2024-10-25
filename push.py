import firebase_admin
from firebase_admin import credentials, db
from colorama import init, Fore, Style
import os
import platform
from tqdm import tqdm
import time
from datetime import datetime

# Initialize Colorama for color support
init(autoreset=True)
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
# Custom bar format with green color using colorama
bar_format = "{l_bar}%s{bar}%s| {n_fmt}/{total_fmt} [{elapsed}<{remaining}] {rate_fmt} - {postfix}" % (Fore.GREEN, Fore.RESET)

def start():
    print(Fore.GREEN +'''
 __    _  _______  __   __  _______  
|  |  | ||       ||  |_|  ||       |
|   |_| ||    ___||       ||   _   |
|       ||   |___ |       ||  | |  |  
|  _    ||    ___| |     | |  |_|  |
| | |   ||   |___ |   _   ||       |  
|_|  |__||_______||__| |__||_______|    \n''')
    print(f"[+] Time: {current_time}")
    # Loop with customized green progress bar
    with tqdm(total=100, bar_format=bar_format, ncols=80) as pbar:
        for i in range(100):
            # Simulate work with time.sleep()
            time.sleep(0.01)
            
            # Update progress and set custom postfix text
            pbar.set_postfix_str("Opening Nexo...")
            pbar.update(1)
    print("Nexo opened successfully!")

start()
# Initialize the Firebase Admin SDK
try:
    cred = credentials.Certificate("smidea-b358a-firebase-adminsdk-iqlg7-bff7ab6fe8.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://smidea-b358a-default-rtdb.firebaseio.com/'
    })
except Exception as e:
    print(Fore.RED + f"Error initializing Firebase Admin SDK: {e}")
    exit(1)

# Function to clear the terminal screen
def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Define a callback to capture changes in the database
def listener(event):
    clear_terminal()  # Clear the terminal before showing new data
    
    # Check if there is any data
    if event.data:
        # The data is a dictionary, so we can extract the values
        if isinstance(event.data, dict):
            print(Fore.GREEN + f"New Event Detected!")
            print(Fore.GREEN + f"Event Name: {event.data.get('name')}")
            print(Fore.GREEN + f"Description: {event.data.get('description')}")
            print(Fore.CYAN + f"Timestamp: {event.data.get('timestamp')}")
        else:
            print(Fore.YELLOW + f"Data: {event.data}")
    else:
        print(Fore.RED + "No data in this event.")

# Listen to a specific path in your Firebase Realtime Database
try:
    db.reference('event').listen(listener)
except Exception as e:
    print(Fore.RED + f"Error listening to Firebase Realtime Database: {e}")
    exit(1)

# Keep the script running to continuously listen to changes
try:
    print(Fore.BLUE + "Listening for changes in Firebase Realtime Database...")
    while True:
        pass
except KeyboardInterrupt:
    print(Fore.RED + "Listener stopped.")
