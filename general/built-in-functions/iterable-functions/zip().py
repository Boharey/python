
"""
          How zip() Works Internally
    The zip() function essentially creates tuples
    by pairing elements from each iterable at the
    same index position. It stops when the shortest
    iterable is exhausted, making it an efficient way
    to pair data without needing to worry about uneven lengths.
  """
  

numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
combined = zip(numbers1, numbers2) #returns <zip object at 0x779a30f02340>
# print(list(combined))  # Output: [(1, 10), (2, 20), (3, 30)]
print(dict(combined))


# Advanced Use Cases and Examples

# 1. Iterate Over Multiple Lists Simultaneously
def use_one() -> None:
  print("\n1. Iterate Over Multiple Lists Simultaneously")
  names = ["Alice", "Bob", "Charlie"]
  ages = [25, 30, 35]
  cities = ["New York", "Los Angeles", "Chicago"]
  for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}.")

# 2. Combining with list(), tuple(), or dict() to Form Different Data Structures

def use_two() -> None:
  print("\n2. Combining with list(), tuple(), or dict() to Form Different Data Structures")
  numbers1 = [1, 2, 3]
  numbers2 = [10, 20, 30]
  combined = zip(numbers1, numbers2)
  print(dict(combined))
  # print(list(combined)) there was a error but i dont know the exact cause
  
  
# 3. You can use zip() to flatten a list of lists, similar to transposing a matrix.
def use_three() -> None:
  print("\n3. You can use zip() to flatten a list of lists, similar to transposing a matrix.")
  matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
  print(matrix)
  # Transpose rows and columns
  transposed = list(zip(*matrix))
  print(transposed)  # Output: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
  
use_one()
use_two()
use_three()


#understanding unzipping process
def use_zip_to_unzip() -> None:
  print("\n4. use zip to unzip")
  zipped = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
  r1,r2,r3 = zip(*zipped)
  print(r1,r2,r3,sep="\n")

use_zip_to_unzip()


##important part 
from itertools import zip_longest
def overWriteBuiltinPropertYofzip() -> None:
  list1 = [1, 2, 3]
  list2 = ['a', 'b']
  combined = list(zip_longest(list1, list2, fillvalue=None))
  print(combined)  # Output: [(1, 'a'), (2, 'b'), (3, None)]

print()