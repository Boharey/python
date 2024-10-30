import os
class Book:
    def __init__(self, title: str, author: str, available: bool = True):
        self.title = title
        self.author = author
        self.available = available  # Initially, the book is available

    def display_info(self) -> None:
        print(f"Title: {self.title}, Author: {self.author}, Status: {'Available' if self.available else 'Not Available'}\n")

    def borrow_book(self) -> bool:
        if self.available:
            self.available = False  # Set the book as not available
            return True
        return False

    def return_book(self) -> None:
        self.available = True  # Set the book as available


class Student:
    def __init__(self, name: str, student_id: str):
        self.name = name  # Name of the student
        self.student_id = student_id  # Unique 5-number ID of the student
        self.books_borrowed: list[Book] = []  # List of borrowed books

    def borrow_book(self, book: Book) -> None:
        if book.borrow_book():  # If the book is available, mark it as borrowed
            self.books_borrowed.append(book)
            print(f"{self.name} borrowed '{book.title}'\n")
        else:
            print(f"'{book.title}' is not available\n")

    def return_book(self, book: Book) -> None:
        if book in self.books_borrowed:
            self.books_borrowed.remove(book)
            book.return_book()  # Mark the book as available
            print(f"'{book.title}' successfully returned by {self.name}")
        else:
            print(f"You don't have '{book.title}' to return! Please check again.")

    def display_borrowed_books(self) -> None:
        print(f"{self.name} has borrowed:")
        if not self.books_borrowed:
            print("No books borrowed.")
        else:
            for book in self.books_borrowed:
                print(f"- {book.title}")


# Main section
if __name__ == "__main__":
  
    os.system('clear') #as i use linux this works for me 
    #windows user can use os.system('cls)
    # Create book objects
    book1 = Book(title="Python Basics", author="No. 1")
    book2 = Book(title="Advanced Python", author="No. 2")
    book3 = Book(title="Python for Dummies", author="John the Don")

    # Display book info
    book1.display_info()
    book2.display_info()
    book3.display_info()

    # Create student objects
    student1 = Student(name="Safal", student_id="11455")
    student2 = Student(name="Subesh", student_id="13556")
    student3 = Student(name="Sabin", student_id="14573")

    # Borrow books
    student1.borrow_book(book2)
    student2.borrow_book(book1)
    student3.borrow_book(book1)  # This should print that the book is not available
    student1.borrow_book(book3)
    
    student1.display_borrowed_books()
    # Return books
    student1.return_book(book2)
    student1.return_book(book1)  # This should print a message that the student doesn't have the book
