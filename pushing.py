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
name = input(Fore.GREEN + "[+] NAME: ")
description = input(Fore.GREEN + "[+] DESCRIPTION: ")
# Initialize the Firebase Admin SDK
try:
    cred = credentials.Certificate("smidea-b358a-firebase-adminsdk-iqlg7-bff7ab6fe8.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://smidea-b358a-default-rtdb.firebaseio.com/'
    })
except Exception as e:
    print(f"Error initializing Firebase Admin SDK: {e}")
    exit(1)

# Function to send data to the Firebase Realtime Database
def send_data_to_db(path, data):
    try:
        ref = db.reference(path)
        ref.set(data)
        print(f"Data sent to {path}: {data}")
    except Exception as e:
        print(f"Error sending data to Firebase Realtime Database: {e}")

# Example: Sending data to the "event" node
data_to_send = {
    'name': name,
    'description': description,
    'timestamp': current_time
}

# Send the data to the 'event' path in the database
send_data_to_db('event', data_to_send)
