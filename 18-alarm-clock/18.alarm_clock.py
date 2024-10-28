import time
import datetime
import pygame

def play_alarm(alarm_file):
    """yo chai alarm chalaune ho hai"""
    pygame.mixer.init() # initialize garaune 
    pygame.mixer.music.load(alarm_file)
    pygame.mixer.music.play(-1)  # Play indefinitely until stopped
    print("Press Enter to stop the alarm.")
    input()  # Wait for Enter key to stop the alarm
    pygame.mixer.music.stop()  # Stop the alarm
    print("Alarm stopped.")

def set_alarm(alarm_time):
    print(f"Alarm set for: {alarm_time}")
    alarm_file = "alarm.mp3"
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        if current_time == alarm_time:
            print("WAKE UP")
            # alarm bajaunw lai yo ho
            play_alarm(alarm_file)
            break  # alarm sakkesi baira aune

        print(current_time)
        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter an alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
