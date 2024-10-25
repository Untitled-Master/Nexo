# Nexo

Nexo is a simple Python-based app that interacts with Firebase Realtime Database to listen for data changes and send new events to the database. It features a dynamic progress bar on startup and allows users to input event data, which is then sent to the Firebase database.

## Features

- **Dynamic Terminal UI**: Displays a startup progress bar using `tqdm` with custom color formatting (via `colorama`).
- **Firebase Realtime Database Integration**: Sends and listens for event changes in Firebase Realtime Database.
- **Cross-Platform**: The terminal clear function works across Windows, macOS, and Linux.

## Requirements

To run this project, you need to have the following Python libraries installed:

- [firebase-admin](https://github.com/firebase/firebase-admin-python)
- [tqdm](https://tqdm.github.io/)
- [colorama](https://pypi.org/project/colorama/)

You can install them by running:

```bash
pip install firebase-admin tqdm colorama
```

Additionally, you need a Firebase project with a Realtime Database set up. Download your Firebase Admin SDK credentials JSON file from your Firebase console.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Untitled-Master/Nexo.git
   cd Nexo
   ```

2. Place your Firebase Admin SDK JSON credentials (`smidea-b358a-firebase-adminsdk-iqlg7-bff7ab6fe8.json`) into the project directory.

3. Run the script:
   ```bash
   python push.py
   or 
   python pushing.py
   ```

   You will see a progress bar with a green color when opening the app:
   
   ```
   __    _  _______  __   __  _______
   |  |  | ||       ||  |_|  ||       |
   |   |_| ||    ___||       ||   _   |
   |       ||   |___ |       ||  | |  |
   |  _    ||    ___| |     | |  |_|  |
   | | |   ||   |___ |   _   ||       |
   |_|  |__||_______||__| |__||_______|    
   ```

4. Enter event details when prompted:
   ```
   [+] NAME: My Event
   [+] DESCRIPTION: This is a test event
   ```

5. The event will be sent to your Firebase Realtime Database, and any changes to the `event` path will trigger a listener callback, clearing the terminal and displaying the event data.

## Firebase Setup

1. Go to the [Firebase Console](https://console.firebase.google.com/) and create a project.
2. Set up a Realtime Database.
3. In the project settings, generate an Admin SDK key and download the JSON file. Place it in the project directory.

## Contribution

Feel free to submit issues and pull requests! We welcome contributions to make this project better.

---

