"""This is the main file for the book store application.
It contains the menu"""
from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """


def menu():
    """This displays the menu in the terminal and calls the appropriate
        function based on the user's input."""
    database.create_book_table()

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


def prompt_add_book():
    """This function prompts the user to enter the title and author of a book"""
    name = input('Enter the book title: ').title()
    author = input('Enter the book author: ').title()

    if not name or not author:
        print('Please enter a valid title and author.')
        return
    try:
      database.add_book(name, author)
    except Exception as e:
      print(f"An error occurred: {e}")

def list_books():
    """The instructor only used a loop to print the books in the database.
    I used a list comprehension to get the titles of the books."""
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_read_book():
    """This function prompts the user to enter the title of a book they just read."""
    name = input('Enter the title of the book you just read: ').title()

    database.mark_book_as_read(name)


def prompt_delete_book():
    """This function prompts the user to enter the title of a book they want to delete."""
    name = input('Enter the title of the book you want to delete: ').title()

    database.delete_book(name)


def get_book_title():
    """This function returns a list of the titles of the books in the database."""
    return [book[0] for book in database.books_file]


menu()
