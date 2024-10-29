# Library Management System

A simple library management system built using Python's Object-Oriented Programming (OOP) concepts. This project demonstrates the use of classes, objects, and methods to simulate a library where students can borrow and return books.

## Table of Contents

- [Features](#features)
- [Classes and Methods](#classes-and-methods)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Example Output](#example-output)
- [License](#license)

## Features

- **Books**: Each book has a title, author, and availability status.
- **Students**: Each student has a name, a unique ID, and a record of borrowed books.
- **Borrowing and Returning**: Students can borrow available books and return them when done.
- **Display Information**: Details of each book, including its availability, can be displayed, as well as the list of books borrowed by each student.

## Classes and Methods

### 1. `Book` Class
Represents a book in the library with the following properties and methods:

- **Properties**:
  - `title`: Title of the book
  - `author`: Author of the book
  - `available`: Boolean indicating if the book is available

- **Methods**:
  - `display_info()`: Prints the book's title, author, and availability status.
  - `borrow_book()`: Marks the book as borrowed if it's available and returns `True`; otherwise, returns `False`.
  - `return_book()`: Marks the book as available.

### 2. `Student` Class
Represents a student with the following properties and methods:

- **Properties**:
  - `name`: Name of the student
  - `student_id`: Unique identifier for the student
  - `books_borrowed`: List of books currently borrowed by the student

- **Methods**:
  - `borrow_book(book)`: Allows the student to borrow a book if it is available.
  - `return_book(book)`: Allows the student to return a book they've borrowed.
  - `display_borrowed_books()`: Displays the list of books the student has currently borrowed.

## Getting Started

### Prerequisites

- Python 3.x installed on your system


### Examples cases
    
    ##INPUT SAMPLE
    book1 = Book(title="Python Basics", author="No. 1")
    book2 = Book(title="Advanced Python", author="No. 2")

    # Create Student instance
    student1 = Student(name="Safal", student_id="11455")

    # Borrowing and returning books
    student1.borrow_book(book1)       # Safal borrows "Python Basics"
    student1.return_book(book1)       # Safal returns "Python Basics"


    ## OUTPUT SAMPLE:
    Title: Python Basics, Author: No. 1, Status: Available
    Title: Advanced Python, Author: No. 2, Status: Available

    Safal borrowed 'Python Basics'

    Safal has borrowed:
    - Python Basics

    'Python Basics' successfully returned by Safal

### License
This `README.md` provides a structured overview of the project, explains the classes and their methods, and gives usage instructions for anyone who wants to try it out. 