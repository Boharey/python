"""
    1. Basics of File Handling in Python
In Python, files are opened using the built-in open() function, which returns a file object. The open() function has two main parameters:

    -> filename: The name (and path) of the file you want to work with.
    -> mode: Specifies the purpose (read, write, append, etc.).

Modes in File Handling

    'r' -  Read (default mode). Opens the file for reading; if the file does not exist, it raises an error.
    'w' -  Write. Opens the file for writing; if the file exists, it is overwritten. If not, a new file is created.
    'a' -  Append. Opens the file for appending data; if the file does not exist, it creates a new one.
    'r+' -  Read and Write. Allows both reading and writing.
    'w+' - Write and Read. Similar to w, but also allows reading.
    'a+' - Append and Read. Allows both appending and reading.
    'x' -  Exclusive creation. Creates a new file but raises an error if it already exists.
  """
  

file = open("learn.txt","r")
data = file.read()
print(data,end="")
print(type(data))
file.close()

list = ["apple","ball","cat"]

with open("learn.txt", "a+") as file:
  for item in list:
    file.write(item)

