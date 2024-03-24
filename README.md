#Title: ToDo API with FastAPI, Neon, Poetry, and SQLModel

##Description:

This repository provides a ToDo API built using FastAPI, Neon, Poetry for dependency management, and SQLModel for interacting with a database.

Features:

1.Create, read, update, and delete (CRUD) operations for ToDo items.
2.Dependency management and environment isolation with Poetry.
3.Database interaction and modeling with SQLModel.

Prerequisites:

Python 3.6 or later
Poetry (https://python-poetry.org/)
A database server (e.g., PostgreSQL, MySQL)


Installation:

Clone this repository:

    instialze poetry project

    Create a virtual environment and activate it (recommended):

    Install dependencies:

    poetry install


Configuration:

Create a .env file in the project root directory 

Set the following environment variables in your .env file:

DATABASE_URL=your_database_url
Replace your_database_url with the actual connection string for your database server.

Running the API:

Start the development server:


    poetry run uvicorn main:app --reload
