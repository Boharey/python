import time
import os

my_time = int(input("enter a time in sec : "))


for i in range(my_time,0,-1):
  seconds = i % 60
  minutes = int(i / 60) % 60 
  hours = int(i / 3600) % 24
  # os.system("clear")
  print(f"\r{hours:02}:{minutes:02}:{seconds:02}", end="", flush=True)  
  time.sleep(1)

print("Times up")
