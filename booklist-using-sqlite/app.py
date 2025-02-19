from flask import Flask, render_template, request, redirect, url_for
from main import prompt_add_book, list_books, prompt_read_book, prompt_delete_book

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            prompt_add_book()
            return render_template("book_added.html")
        except Exception as e:
            print(f"Error adding book: {e}")
            return render_template("error.html", error=str(e))
    return render_template("index.html")

@app.route("/list")
def list_books_route():
    try:
        books = list_books()
        return render_template("book_list.html", books=books)
    except Exception as e:
        print(f"Error listing books: {e}")
        return render_template("error.html", error=str(e))

@app.route("/read", methods=["POST"])
def read_book_route():
    try:
        prompt_read_book()
        return render_template("book_updated.html")
    except Exception as e:
        print(f"Error marking book as read: {e}")
        return render_template("error.html", error=str(e))

@app.route("/delete", methods=["POST"])
def delete_book_route():
    try:
        prompt_delete_book()
        return render_template("book_deleted.html")
    except Exception as e:
        print(f"Error deleting book: {e}")
        return render_template("error.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)