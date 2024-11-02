#understading the working of print function

# default working of print fucntion
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

import time,sys,os


visual_representaion_of_flush = """
+-------------------------------------------------+
|                Output Buffer                    |
| +---------------------------------------------+ |
| | 0 | 1 | 2 | 3 | 4 |   |   |   |   |   |   |   |   
| +---------------------------------------------+ |
|                                                 |
|                    (Flush)                      |
|               FALSE /   \  TRUE                 |
|          +--------+     +--------+              |
|Print after buffer Full    Print to Console      |
|          +--------+     +--------+              |
|                                                 |
+-------------------------------------------------+

"""

def workingOfFlush():
  os.system('clear')
  # Example with flush=False
  print("Example with flush=False:")
  for i in range(5):
    print(i, end=" ", flush=False)  # Buffered output
    time.sleep(1)  # Simulate delay
  print("\nOutput may appear only after the loop ends when flush is False.\n")

  # Adding a delay to separate the two examples clearly
  time.sleep(2)

  # Example with flush=True
  print("Example with flush=True:")
  for i in range(5):
    print(i, end=" ", flush=True)  # Immediate output
    time.sleep(1)  # Simulate delay
  print("\nOutput should appear immediately one-by-one when flush is True.")
  
print(visual_representaion_of_flush)
# workingOfFlush()