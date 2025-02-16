"""This is the main file for the book store application. It contains the menu"""
from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """

class Book:
    """I created a class for the Book object. I also created a class method to create
    a new instance of the Book class"""
    def __init__(self, title, author, read):
        self.title = title
        self.author = author
        self.read = read

    @classmethod
    def from_input(cls):
        """This class method creates a new instance of the Book class using the user's input"""
        title= input('Enter the book title: ').title() # Added .title() here
        author = input('Enter the book author: ').title() # Added .title() here
        return cls(title, author, False)

def menu():
    """This displays the menu in the terminal and calls the appropriate"""
    try:
        user_input = input(USER_CHOICE).lower()
        while user_input != 'q':
            if user_input == 'a':
                prompt_add_book()
            elif user_input == 'l':
                list_books()
            elif user_input == 'r':
                prompt_read_book()
            elif user_input == 'd':
                prompt_delete_book()
            else:
                print('Please select a valid option')
            user_input = input(USER_CHOICE).lower()
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")


def get_book_title():
    """This function returns a list of the titles of the books in the database"""
    return [book[0] for book in database.books]


def prompt_add_book():
    """Where I messed up here was that I was overwriting the new_book variable with each new input.
    I should have appended the new_book to the database.books list.
    I was able to accomplish this by using the Book.from_input() method to create a new instance
    of the Book class using
    the @classmethod."""
    # new_book.title = input('Enter the book title: '),
    # new_book.author = input('Enter the book author: ')
    # new_book.read = False
    new_book = Book.from_input()
    if new_book.title not in get_book_title():
        database.books.append([new_book.title, new_book.author, new_book.read])
    else:
        print('\nBook already in database, please review the book title and try again. \n')

def list_books():
    """This function prints the books in the database"""
    if not database.books:
        print('No books in the database')
    else:
        print(database.books)

def prompt_read_book():
    """This function marks a book as read"""
    read_book = input('Enter the title of the book you just read: ').title() # Added .title() here
    # new_book = Book.from_input() I realized that I don't need
    # to create a new instance of the Book class here.
    # if new_book.title not in get_book_title():
    #     database.books.append([new_book.title, new_book.author, new_book.read])
    # else:
    #     database.books.append([new_book.title, new_book.author, new_book.read = True])
    # I was foolish enough to try this, and it obviously didn't work.
    # I was trying to change the value of the read attribute
    # book = [book for book in database.books if book[0] == read_book]
    # book = True
    for book in database.books:
        if book[0] == read_book:
            book[2] = True
            print(f'{book[0]} has been marked as read.')
            return
    print(f'{read_book} not found in database.')


def prompt_delete_book():
    """This function deletes a book from the database"""
    delete_book = input('Enter the title of the book you want to delete: ').title() # Added .title() here

    for book in database.books:
        if book[0] == delete_book:
            database.books.remove(book)
            print(f'{delete_book} has been deleted from the database.')
            return
    print(f'{delete_book} not found in database.')
    return


menu()
