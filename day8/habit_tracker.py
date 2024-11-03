import os

# Constants
FILE_NAME = "habit_tracker.txt"
DAILY_GOALS = {"Exercise": False, "Read for 30 minutes":False , "Code for 1 hour": False}


def log_habits(date,daily_status):
  with open(FILE_NAME,"a") as file:
    file.write(f"Date : {date}\n")
    for habit in DAILY_GOALS:
      status = "completed" if daily_status[habit] else "not completed"
      file.write(f"{habit} : {status}")
    file.write("----\n")
    
if __name__ == "__main__":
  date: str
  date = input("enter date:")
