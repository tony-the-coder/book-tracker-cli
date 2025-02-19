from utils import database
from flask import request

def prompt_add_book():
    """This function gets the title and author from the web form."""
    name = request.form['name'].title()
    author = request.form['author'].title()

    if not name or not author:
        print('Please enter a valid title and author.')
        return
    try:
        database.add_book(name, author)
    except Exception as e:
        print(f"An error occurred: {e}")

def list_books():
    """This function returns the list of books from the database."""
    return database.get_all_books()

def prompt_read_book():
    """This function gets the title of the book to mark as read from the web form."""
    name = request.form['name'].title()
    database.mark_book_as_read(name)

def prompt_delete_book():
    """This function gets the title of the book to delete from the web form."""
    name = request.form['name'].title()
    database.delete_book(name)