# Library API Documentation

This API provides functionalities to manage a library system, including CRUD operations for book categories and books.

## Endpoints

- **Book Categories:**
  - `GET /categories/`: Retrieve all book categories.
  - `POST /categories/`: Create a new book category.
  - `GET /categories/{id}/`: Retrieve details of a specific book category.
  - `PUT /categories/{id}/`: Update details of a specific book category.
  - `DELETE /categories/{id}/`: Delete a specific book category.

- **Books:**
  - `GET /books/`: Retrieve all books.
  - `POST /books/`: Create a new book.
  - `GET /books/{id}/`: Retrieve details of a specific book.
  - `PUT /books/{id}/`: Update details of a specific book.
  - `DELETE /books/{id}/`: Delete a specific book.

## Schema

For the database schema, refer to the [Entity Relationship Diagram (ERD)](erd_diagram_link).

## Postman Documentation

Explore the API endpoints and test requests using the Postman documentation available [here](postman_documentation_link).

## Running Locally

To run the API locally, follow these steps:

1. Clone the repository:

    
    - git clone [Repo](https://github.com/F0laf0lu/LibraryApi.git)
    
2. Install dependencies:

    
    - pip install -r requirements.txt
    

3. Run migrations:

    
    - python manage.py migrate
    


4. Start the development server:
    
    - python manage.py runserver
    

## Running Tests

To run the tests for the API, execute the following command:

    
    - python manage.py test
    
