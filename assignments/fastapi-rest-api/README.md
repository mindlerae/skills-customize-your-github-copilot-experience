# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will learn how to build a REST API with FastAPI. They will create HTTP endpoints, work with JSON request and response data, and add validation for a small book catalog.

## 📝 Tasks

### 🛠️ Create the API and a Read Endpoint

#### Description
Set up the FastAPI application in `starter-code.py` and implement the first endpoint for reading the available books.

#### Requirements
Completed program should:

- Start a FastAPI application named `app`
- Return all books from `GET /books`
- Return a single book from `GET /books/{book_id}`
- Return a clear `404` response when a requested book does not exist
- Run locally with Uvicorn and expose the automatic documentation at `/docs`


### 🛠️ Add Create, Update, and Delete Operations

#### Description
Complete the remaining CRUD operations so clients can manage the in-memory book catalog.

#### Requirements
Completed program should:

- Create a book with `POST /books`
- Update a book with `PUT /books/{book_id}`
- Delete a book with `DELETE /books/{book_id}`
- Return appropriate HTTP status codes for successful creation, updates, and deletions
- Return a clear `404` response when updating or deleting a missing book


### 🛠️ Validate Requests and Test the API

#### Description
Use Pydantic models to validate incoming JSON data, then test every endpoint using FastAPI's interactive documentation or a tool such as `curl`.

#### Requirements
Completed program should:

- Require a non-empty title and author when creating a book
- Reject invalid request data with FastAPI validation errors
- Return JSON responses with a consistent book shape containing `id`, `title`, and `author`
- Demonstrate successful and unsuccessful requests for each CRUD operation
- Include at least three test examples in a short comment block or a separate text file
