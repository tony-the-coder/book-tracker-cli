# Book Tracker CLI

A command-line interface (CLI) application to manage a list of books. This application allows you to add books, list them, mark them as read, delete them, and export them to a Markdown file for use with Obsidian. This allows you to integrate your book data with your personal knowledge base and use Obsidian's features (such as Dataview) to view and interact with the data. Eventually, a GUI version will be created and other features will be implemented.

## Features

*   **Add Books:** Easily add new books to your list by providing the title and author.
*   **List Books:** View all the books currently in your database.
*   **Mark as Read:** Update the status of a book to indicate that you've read it.
*   **Delete Books:** Remove books from your list.
*   **Markdown Export:** Export your book list to a Markdown file that's compatible with Obsidian, allowing you to integrate your book data with your personal knowledge base and use Obsidian's features (such as Dataview) to view and interact with the data.
*   **Rating System:** Add a rating (e.g., 1 to 5) for each book.
*   **Author-Related Features:**
    *   List all books by a given author.
    *   Search for books by a specific author.

## Planned Features

*   **GUI:** A graphical user interface will be added to the application for a better user experience.
*   **Persistence:** Data will be stored in a file (JSON, CSV, database) to persist the data.
*   **Expanded Export:** Add more robust export features for more customization and add all metadata for the application.
*   **Searching:** Add search by title, rating, author and other metadata.
*    **User Interface Improvements:** Improved user interactions will be added.
*  **Testing:** Adding unit tests to ensure program stability.
*   **Favorite Author:** A function to list books by a favorite author.
*   **Books by Author:** A feature to list books by the same author as another input.

## How to Use

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/<your-username>/book-tracker-cli.git
    ```
    (Replace `<your-username>` with your actual GitHub username)

2.  **Navigate to the project directory:**

    ```bash
    cd book-tracker-cli
    ```

3.  **Run the application:**

    ```bash
    python main.py
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

## Code Structure

*   `main.py`: Contains the main logic of the application, including input prompts and the `menu` function, as well as the Book class and functions.
*   `utils/database.py`: Contains the in-memory `books` list that stores the book information.

## Improvements

This is a basic application that stores information in memory, meaning all data is lost when the program closes. This current version does not have data persistence, so data will be lost. Here are some areas for improvement:

*   **Persistence:** Store data in a file (JSON, CSV, database) to persist the data.
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
