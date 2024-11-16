# Python Function Examples with *args and **kwargs

# Example 1: Using *args to pass variable positional arguments
def greet(*args):
    """
    Greets each person passed as a positional argument.
    Args:
    *args: Variable number of positional arguments (names).
    """
    for name in args:
        print(f"Hello, {name}!")
    print("\n")

# Example 2: Using **kwargs to pass variable keyword arguments
def print_info(**kwargs):
    """
    Prints the provided keyword arguments.
    Args:
    **kwargs: Variable number of keyword arguments (key-value pairs).
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print("\n")

# Example 3: Combining *args and **kwargs in one function
def display_info(*args, **kwargs):
    """
    Displays both positional and keyword arguments.
    Args:
    *args: Positional arguments.
    **kwargs: Keyword arguments.
    """
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    

# Test the functions
greet("Utsav", "Mohit", "Sabin", "Safal")
print_info(name="Alice", age=25, city="New York")
display_info("Alice", "Bob", name="Charlie", age=30)
