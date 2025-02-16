# Book Tracker CLI

A command-line interface (CLI) application to manage a list of books. This application allows you to add books, list them, mark them as read, delete them, and export them to a Markdown file for use with Obsidian. This allows you to integrate your book data with your personal knowledge base and use Obsidian's features (such as Dataview) to view and interact with the data. Eventually, a GUI version will be created and other features will be implemented.  This version of the application utilizes a text file (`books.txt`) for data persistence.

## Features

*   **Add Books:** Easily add new books to your list by providing the title and author.
*   **List Books:** View all the books currently in your database.  Displays a message if the book list is empty.
*   **Mark as Read:** Update the status of a book to indicate that you've read it.
*   **Delete Books:** Remove books from your list.
*   **Markdown Export:** Export your book list to a Markdown file that's compatible with Obsidian, allowing you to integrate your book data with your personal knowledge base and use Obsidian's features (such as Dataview) to view and interact with the data.
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
    python app.py  # Or python app.py if using a specific version
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

This repository contains different versions of the book tracker application, demonstrating the evolution of the code:

*   **`main.py` (or `app.py` in some versions):** Contains the main logic of the application, including input prompts and the `menu` function.  Different versions of this file demonstrate different approaches to the application's core functionality.
*   **`utils/database.py`:** Contains the functions for interacting with the book data. This version uses a `books.txt` file for persistent storage.

##  Key Improvements and Learnings (Current Version)

*   **File-Based Persistence:** The current version uses a `books.txt` file to store book data, allowing the data to persist between sessions. The file format is:

    ```
    name,author,read\n
    name,author,read\n
  ...
    ```

    The `read` status is represented as `0` for "not read" and `1` for "read."

*   **Error Checking:** The application includes error checking, such as handling the case where the book list is empty.  More comprehensive error handling is planned for future versions.

## Improvements (Planned)

*   **Persistence:**  While this version uses a text file, future versions may explore other persistence methods (JSON, CSV, or a more robust database).
*   **Error Handling:** Enhanced error handling and more robust input validation.
*   **User Interface:** Adding more features for better user interaction.
*   **Search Functionality:** Ability to search books by title, author, etc.
*   **Testing:** Adding unit tests.

## Contributing

If you would like to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgment

This project was built based on the Milestone 2 brief of "The Complete Python Course | Learn Python by Doing in 2025" by Codestars and Jose Salvatierra on Udemy. The project was completed without viewing the video or provided solution, using only the text brief for the milestone.