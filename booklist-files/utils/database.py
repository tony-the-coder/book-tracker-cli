"""
Concerned with storing and retrieving data from a csv file.
Format of the csv file:

name,author,read\n
name,author,read\n
name,author,read\n

"""
books_file = 'books.txt'

"""These functions are from the instructor's solution."""

def create_book_table():
    """Create the books.txt file if it doesn't exist and is called
    from app.py."""
    with open(books_file, 'w'):
        pass # Just to create the file if it doesn't exist.



def add_book(name, author):
    """Add a book to the list of books."""
    with open(books_file, 'a') as file:
        file.write(f'{name},{author},0\n')



def get_all_books():
    """Return all books in the books.txt file."""
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()] # [['name', 'author', '0'],
        # ['name', 'author', '0']]

    return [ #[['name', 'author', 'read'], ['name', 'author', 'read']]
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]



def mark_book_as_read(name):
    """Marks a book as read."""
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = "1"
    _save_all_books(books)


def _save_all_books(books):
    """The reason that there is an underscore before the function name is to indicate that
    this function is private and should not be called from outside this module."""
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)




