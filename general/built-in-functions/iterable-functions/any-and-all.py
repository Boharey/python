"""The any() and all() functions in Python are built-in functions
  that are particularly useful when working with iterables
  (like lists, tuples, sets, or any other collection). 
  They help in quickly checking the truthiness of elements within these iterables.
"""

def working_of_any():
  """How it Works:
    any() iterates over each element in the iterable.
    As soon as it finds a True element, it stops and returns True.
    If no True elements are found, it returns False.
  """
  print("\nworking of any : ")
  numbers = [1, 2, 3, 0]
  print(any(num > 2 for num in numbers))  # Output: True (since 3 is greater than 2)

def working_of_all():
  """How it Works:
    all() iterates over each element in the iterable.
    If it finds any False element, it stops and returns False.
    If all elements are True, it returns True.
  """
  print("\nworking of all : ")
  numbers = [2,4,6,8,10]
  print(all(num % 2 == 0 for num in numbers)) #returns true as all are even
  
if __name__ == "__main__":
  working_of_any()
  working_of_all()