# this is about the builtin function sum() that takes iterable object as its input 

# sum(iterable, start=0)

#for integers

list1 = list(num for num in range(1,100,2))
#odd numbers till 100
print(list1)
print(sum(list1)) #2500
print(sum(list1,start = -100)) #2400


# Attempting to sum strings
# strings = ['Hello', ' ', 'World']
# result = sum(strings)  # Output: Error: unsupported operand type(s) for +: 'int' and 'str'
# print(result)


#but can use a trick for strings like:
my_name = ["Utsav", " ", "Bohara"]
result1 = sum(my_name," ") 
"""
    it works because it treats the first argument 
    as a string to which the other strings are concatenated.
"""
 