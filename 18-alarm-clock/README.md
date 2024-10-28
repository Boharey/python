# Python Alarm Clock Documentation

## Overview

The **Python Alarm Clock** is a simple command-line application that allows users to set alarms that play a sound at a specified time. This project utilizes the `pygame` library for audio playback and demonstrates the handling of time and date functions in Python.

## Features

- **Set Alarm**: Users can set an alarm for any time in the format HH:MM:SS.
- **Alarm Sound**: The application plays an audio file when the alarm time is reached.
- **Stop Alarm**: Users can stop the alarm by pressing the Enter key.

## Prerequisites

To run this project, you need to have the following installed on your system:

- **Python 3.x**
- **pygame library**

## Installation

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
cd <repository-directory>

Step 2: Install Dependencies

Install the required pygame library using pip:

bash

pip install pygame

Step 3: Add Alarm Sound File

Ensure you have an audio file named alarm.mp3 located in the same directory as the script. You can use any MP3 file of your choice by renaming it to alarm.mp3.
Usage
Running the Application

    Execute the Script: Run the following command in your terminal or command prompt:

    bash

    python alarm_clock.py

    Set Alarm Time: When prompted, enter the desired alarm time in the format HH:MM
    (e.g., 14:30:00).

    Alarm Notification: The application will print the current time and notify you when the alarm goes off.

    Stopping the Alarm: Press the Enter key to stop the alarm when it sounds.

Example Output

sql

Enter an alarm time (HH:MM:SS): 14:30:00
Alarm set for: 14:30:00
Current time: 14:29:59
Current time: 14:30:00
WAKE UP
Press Enter to stop the alarm.

License

This project is licensed under the MIT License.