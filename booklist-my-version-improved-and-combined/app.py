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
    """
    Represents a book with title, author, and read status.
    """
    def __init__(self, title, author, read):
        """
        Initializes a new Book object.

      :param title: The title of the book.
      :param author: The author of the book.
      :param read: Boolean indicating if the book has been read.
        """
        self.title = title
        self.author = author
        self.read = read

    @classmethod
    def from_input(cls):
        """
        Creates a new Book object from user input.

      :return: A new Book object.
        """
        title = input('Enter the book title: ').title()
        author = input('Enter the book author: ').title()
        return cls(title, author, False)

def menu():
    """
    Displays the menu and interacts with the user.
    """
    try:
        user_input = input(USER_CHOICE).lower()
        while user_input!= 'q':
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

def prompt_add_book():
    """
    Prompts the user for book information and adds it to the database.
    """
    new_book = Book.from_input()
    database.add_book(new_book.title, new_book.author)

def list_books():
    """
    Lists all books in the database.
    """
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")

def prompt_read_book():
    """
    Prompts the user for a book title and marks it as read.
    """
    name = input('Enter the title of the book you just read: ').title()
    database.mark_book_as_read(name)

def prompt_delete_book():
    """
    Prompts the user for a book title and deletes it from the database.
    """
    name = input('Enter the title of the book you want to delete: ').title()  # Added.lower() here
    database.delete_book(name)

menu()