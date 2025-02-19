# Book Tracker

A command-line interface (CLI) application and basic web GUI to manage a list of books. This application allows you to add books, list them, mark them as read, and delete them. It features a SQLite database for persistent storage and includes comprehensive error handling and logging.

## Features

*   **Command-line Interface:**
    *   Add books: Add new books to your list by providing the title and author.
    *   List books: View all the books currently in your database.
    *   Mark as read: Update the status of a book to indicate that you've read it.
    *   Delete books: Remove books from your list.

*   **Web Interface (basic):**
    *   Add books: Add new books through a web form.
    *   List books: View all books in a web page.

## Planned Features

*   **GUI Enhancements:** Improve the web interface with more features and better user experience.
*   **Export:** Export your book list to various formats (e.g., Markdown, CSV).
*   **Search:** Add search functionality to find books by title, author, or other criteria.
*   **User Accounts:** Implement user authentication and accounts.
*   **Testing:** Add unit tests to ensure program stability.

## How to Use

### Command-line Interface

1.  Clone the repository:

    ```bash
    git clone [https://github.com/tony-the-coder/book-tracker-cli.git](https://github.com/tony-the-coder/book-tracker-cli.git)
    ```

2.  Navigate to the project directory:

    ```bash
    cd book-tracker
    ```

3.  Run the application:

    ```bash
    python main.py
    ```

4.  Follow the on-screen prompts:

    ```
    Enter:
    - 'a' to add a new book
    - 'l' to list all books
    - 'r' to mark a book as read
    - 'd' to delete a book
    - 'q' to quit
    Your choice: 
    ```

### Web Interface

1.  Make sure you have Flask installed:

    ```bash
    pip install Flask
    ```

2.  Run the Flask application:

    ```bash
    python app.py
    ```

3.  Access the web interface in your browser at `http://127.0.0.1:5000/`.

## Code Structure

*   **`app.py`:** Contains the Flask application setup, routing, and template rendering.
*   **`main.py`:** Contains the core logic for interacting with the user and the database.
*   **`utils/database.py`:** Contains functions for interacting with the SQLite database.
*   **`utils/database_connection.py`:** Defines the `DatabaseConnection` class for managing database connections.
*   **`templates/`:** Contains HTML templates for the web interface.
*   **`static/`:** Contains static files (CSS, JavaScript) for the web interface.

## Key Improvements

*   **Web Interface:** Added a basic web interface using Flask, Tailwind CSS, and Flowbite.
*   **Database Interaction:** The application uses a SQLite database for persistent storage.
*   **Error Handling:** Includes comprehensive error handling and logging.

## Contributing

If you would like to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.