#map

def understanding_map():
  def square(x: int) -> int:
    return x ** 2
  
  numbers = [1, 2, 3, 4]
  squared_numbers = map(square,numbers)
  print(squared_numbers) #<map object at 0x7f7411462200>
  print(list(squared_numbers)) #[1, 4, 9, 16]

def understanding_filter():
  def isEven(x: int) -> int:
    return (x & 1) == 0 #true for even similar to x%2 == 0
  numbers = [1, 2, 3, 4]
  filtered_num = filter(isEven,numbers)
  print(filtered_num)
  print(list(filtered_num))
    
if __name__=="__main__":
  understanding_filter()
  understanding_map()
  
#filter(function(boolean),iterable(list,tuple,dict,...))

#map(function,iterable(list,tuple,dict,...))