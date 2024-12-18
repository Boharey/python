"""
    len() is a versatile and quick way to count elements.
    It is compatible with any data structure that can be counted (if it implements __len__()).
"""

# its use case in normal data structures is very easy so lets start directly with its use in user defined class

class Book():
  def __init__(self,pages: int,name: str = "unnamed") -> None:
    self.name = name
    self.pages = pages

  def __len__(self) -> int:
    return self.pages

b1 = Book(pages = 300)
print(len(b1))

class Bike():
  def __init__(self,cost: int,company: str = "unnamed") -> None:
    self.company = company
    self.price = cost # in thousands(K)
  
  def __len__(self) -> int:
    return self.price
  #using len() function now causes to return the cost if the bike 
  
bk1 = Bike(10)
print(len(bk1)) # returns 10
  