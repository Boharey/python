#this is simple number guessing game here we will

import random

#can modify to select a custom range of integers
random_number = random.randint(1, 100)
# print(random_number)
hot: list[int] = []

while True:
  number: int = int(input("Enter your guess : "))
  if(number == random_number):
    print("you won")
    break
  
  for i in range(random_number-10,random_number+10):
    hot.append(i)
  
  if(number in hot):
    print("hot")
  else:
    print("cold")