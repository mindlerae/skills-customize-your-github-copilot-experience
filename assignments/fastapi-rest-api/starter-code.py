"""Starter code for the FastAPI REST API assignment.

Install dependencies with:
    pip install fastapi uvicorn

Run the API with:
    uvicorn starter-code:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class Book(BaseModel):
    title: str
    author: str


books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Catalog API"}


@app.get("/books")
def list_books():
    """Return every book in the catalog."""
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Return one book, or add a 404 response when it is missing."""
    # TODO: Find the book with the matching ID.
    # TODO: Raise HTTPException(status_code=404, detail="Book not found") if needed.
    return {"message": "Implement this endpoint"}


@app.post("/books", status_code=201)
def create_book(book: Book):
    """Add a book to the catalog and assign it the next available ID."""
    # TODO: Create an ID, add the book to books, and return the new book.
    return {"message": "Implement this endpoint"}


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    """Replace an existing book."""
    # TODO: Find and replace the book, or return a 404 response.
    return {"message": "Implement this endpoint"}


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """Delete a book from the catalog."""
    # TODO: Remove the book, or return a 404 response.
    return {"message": "Implement this endpoint"}
