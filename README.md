# Book Tracker CLI

A command-line interface (CLI) application to manage a list of books. This application allows you to add books, list them, mark them as read, delete them, and eventually export them to a Markdown file for use with Obsidian. This allows you to integrate your book data with your personal knowledge base and use Obsidian's features (such as Dataview) to view and interact with the data.  Different versions of the application demonstrate various data persistence methods, including using a SQLite database. Eventually, a GUI version will be created and other features will be implemented.

## Features

*   **Add Books:** Easily add new books to your list by providing the title and author. Includes error handling for duplicate entries.
*   **List Books:** View all the books currently in your database. Displays a message if the book list is empty.
*   **Mark as Read:** Update the status of a book to indicate that you've read it.
*   **Delete Books:** Remove books from your list.
*   **Markdown Export:** Export your book list to a Markdown file that's compatible with Obsidian.
*   **Rating System:** Add a rating (e.g., 1 to 5) for each book.
*   **Author-Related Features:**
    *   List all books by a given author.
    *   Search for books by a specific author.

## Planned Features

*   **GUI:** A graphical user interface will be added to the application for a better user experience.
*   **Expanded Export:** Add more robust export features for more customization and add all metadata for the application.
*   **Searching:** Add search by title, rating, author and other metadata.
*   **User Interface Improvements:** Improved user interactions will be added.
*   **Testing:** Adding unit tests to ensure program stability.
*   **Favorite Author:** A function to list books by a favorite author.
*   **Books by Author:** A feature to list books by the same author as another input.

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
    python app.py  # Or python main.py if using a specific version
    ```

4.  **Follow the on-screen prompts:**

    The application will guide you through the available options:

    ```
    Enter:
    - 'a' to add a new book
    - 'l' to list all books
    - 'r' to mark a book as read
    - 'd' to delete a book
    - 'e' to export to markdown
    - 'q' to quit
    Your choice:
    ```

## Code Structure and Versions

This repository contains different versions of the book tracker application, demonstrating the evolution of the code and different data persistence methods:

*   **`main.py` or `app.py`:** Contains the main logic of the application.
*   **`utils/database.py`:** Contains the functions for interacting with the book data.

The following data persistence methods are implemented in different versions:

*   **Plain Text (`books.txt`):**  Data is stored in a comma-separated format in a text file.  The `read` status is represented as `0` for "not read" and `1` for "read."
*   **JSON (`books.json`):** Data is stored in JSON format, providing a more structured and flexible way to represent book information.
*   **SQLite Database (`data.db`):** Data is stored in a SQLite database, providing a more robust and efficient way to manage data.

##  Key Improvements and Learnings (Current Versions)

*   **File-Based Persistence:** The application now supports different file-based persistence methods, allowing data to be saved and loaded between sessions.
*   **Data Storage Formats:** The application demonstrates how to work with different data storage formats (plain text, JSON, and SQLite).
*   **Error Checking:** The application includes error checking, such as handling the case where the book list is empty and preventing duplicate book entries. More comprehensive error handling is planned for future versions.

## Improvements (Planned)

*   **GUI:** A graphical user interface will be added to the application for a better user experience.
*   **Expanded Export:** Add more robust export features for more customization and add all metadata for the application.
*   **Searching:** Add search by title, rating, author and other metadata.
*   **User Interface Improvements:** Improved user interactions will be added.
*   **Testing:** Adding unit tests to ensure program stability.
*   **Favorite Author:** A function to list books by a favorite author.
*   **Books by Author:** A feature to list books by the same author as another input.

## Contributing

If you would like to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgment

This project was built based on the Milestone 2 brief of "The Complete Python Course | Learn Python by Doing in 2025" by Codestars and Jose Salvatierra on Udemy. The project was completed without viewing the video or provided solution, using only the text brief for the milestone.