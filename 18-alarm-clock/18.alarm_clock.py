import time
import datetime
import pygame

def play_alarm(alarm_file: str) -> None:
    """Function to play the alarm sound."""
    pygame.mixer.init()
    pygame.mixer.music.load(alarm_file)
    pygame.mixer.music.play(-1)  # Play indefinitely until stopped
    print("Press Enter to stop the alarm.")
    input()  # Wait for Enter key to stop the alarm
    pygame.mixer.music.stop()  # Stop the alarm
    print("Alarm stopped.")

def set_alarm(alarm_time: str) -> None:
    """Function to set the alarm for a specific time."""
    print(f"Alarm set for: {alarm_time}")
    alarm_file = "alarm.mp3"
    
    while True:
        current_time: str = datetime.datetime.now().strftime("%H:%M:%S")
        
        if current_time == alarm_time:
            print("WAKE UP")
            # Play the alarm sound
            play_alarm(alarm_file)
            break  # Exit the loop after handling the alarm

        print(current_time)
        time.sleep(1)

if __name__ == "__main__":
    alarm_time: str = input("Enter an alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
