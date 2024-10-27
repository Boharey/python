import random,time,os


clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')
  
  
# Creating a dictionary to assign ASCII art for dice
dice_art_dict: dict[int,str] = {
    1: """
      +-------+
      |       |
      |   *   |
      |       |
      +-------+""",
    2: """
      +-------+
      | *     |
      |       |
      |     * |
      +-------+""",
    3: """
      +-------+
      | *     |
      |   *   |
      |     * |
      +-------+""",
    4: """
      +-------+
      | *   * |
      |       |
      | *   * |
      +-------+""",
    5: """
      +-------+
      | *   * |
      |   *   |
      | *   * |
      +-------+""",
    6: """
      +-------+
      | *   * |
      | *   * |
      | *   * |
      +-------+"""
}

dice_roll_times:int = int(input("no of times dice is rolled : "))

sum: int = 0

#each dice roll value in a list of size dice_roll_times
for i in range(dice_roll_times):
  clear_screen()
  dice_roll = random.randint(1,6)
  print(dice_roll, end = " ")
  print(dice_art_dict[dice_roll],end =" ",flush=True)
  sum = sum + dice_roll
  time.sleep(2)
print(f"\nsum is : {sum}")
