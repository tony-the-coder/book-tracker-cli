# Book Tracker CLI

A command-line interface (CLI) application to manage a list of books. This application allows you to add books, list them, mark them as read, and delete them. It features a SQLite database for persistent storage and includes comprehensive error handling and logging.

## Features

*   **Add Books:** Easily add new books to your list by providing the title and author. Includes error handling for duplicate entries.
*   **List Books:** View all the books currently in your database. Displays a message if the book list is empty.
*   **Mark as Read:** Update the status of a book to indicate that you've read it.
*   **Delete Books:** Remove books from your list.

## Planned Features

*   **GUI:** A graphical user interface will be added to the application for a better user experience.
*   **Export:** Export your book list to various formats (e.g., Markdown, CSV).
*   **Search:** Add search functionality to find books by title, author, or other criteria.
*   **User Interface Improvements:** Improved user interactions will be added.
*   **Testing:** Adding unit tests to ensure program stability.

## How to Use

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/tony-the-coder/book-tracker-cli.git](https://github.com/tony-the-coder/book-tracker-cli.git)
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd book-tracker-cli
    ```

3.  **Run the application:**

    ```bash
    python app.py
    ```

4.  **Follow the on-screen prompts:**

    The application will guide you through the available options:

    ```
    Enter:
    - 'a' to add a new book
    - 'l' to list all books
    - 'r' to mark a book as read
    - 'd' to delete a book
    - 'q' to quit
    Your choice:
    ```

## Code Structure

*   **`app.py`:** Contains the main logic of the application, including the command-line interface and user interaction.
*   **`utils/database.py`:** Contains functions for interacting with the SQLite database, including adding, retrieving, updating, and deleting book records.
*   **`utils/database_connection.py`:** Defines the `DatabaseConnection` class, which manages the database connection and provides error handling and logging.

## Key Improvements

*   **Database Connection Management:** The `DatabaseConnection` class encapsulates database connection logic, improving code organization and maintainability.
*   **Error Handling:** The application includes comprehensive error handling for database operations, providing informative messages to the user and logging exceptions for debugging.
*   **Type Hints:** Type hints have been added to function signatures to improve code readability and maintainability.

## Contributing

If you would like to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.