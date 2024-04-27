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

![LibraryAPI ERD](https://github.com/F0laf0lu/LibraryApi/assets/119736310/c6869689-77f3-43dc-80d3-d9d88751f546)


For the database schema, refer to the [Entity Relationship Diagram (ERD)]([https://dbdiagram.io/d/TicketWave-6588949689dea627997dfcd1](https://viewer.diagrams.net/?tags=%7B%7D&highlight=FFFFFF&edit=_blank&layers=1&nav=1&title=Library%20ERD.drawio#R7VxRb6M4EP41SHsPWxEoafvY0GR3dele1e3eSfdSueAQXwlGxmmS%2FfU3BhuSmKRkG5o0IEURDMPYnu%2BbD4JxDNudzL8wFI9vqY9DwzL9uWHfGJZ1eWnCtzAsMoNjdjNDwIifmTqF4Qf5haVRnhdMiY%2BTFUdOachJvGr0aBRhj6%2FYEGN0tuo2ouFqqzEKsGb44aFQt%2F5DfD6Ww3LMwv4Vk2CsWu6Y8sgEKWdpSMbIp7MVE57zAY247OIdZhMU4YjDkVvEnjEznP6YczHSa8MawGckvM8CSoMQo5gkZx6dgNlLwGUwQhMSijQvBerJQNCc3Tdsl1HKs63J3MWhgErBkPVpsOFongcm4lY4wf38shg%2Bmzz6OrP%2F5re3wd3F02cZ5QWFU5lfmRu%2BUAnHPuRf7kJThC%2FucYg4oVG%2FONLDkX8t0AWn%2Fv0vzOgDvUURDL6XcMR4cYxG0n1AoHv2TUe5yH0T9vWhyX4mdMo8vGU81rmkJGIB5lscJenF4JZakJn7gukEc7YAh1nBsZxJ42V%2BKSNLk%2FKyylIkmRTkAfM27ihJiSXr0j6XcWRZXihKqhDZ0OVZyzCvBTpfC9RdD5SlRgsEG0sDL0wpi3ZglKUxqkfps8YqKL5YbHL0lPInpYBUG1twAPSDIxJBqWQc8WgYojghqXtmGZPQH6IFnXIVSO31RmSO%2FftMbIQvsG8IwRJJMFG2itPiMApJEMG2B4QTLfYYTqAvQ5Rw6bGRki%2BYcTzfyiGFjGOtINNRyCxxLJfZZY5ZF%2BZmOq3gtytY9uvlr4CCoXOCwnvQdBQFKWarkIi8%2BozGD6r0hCEWNMOs%2F4IzVU2TD4Xu0pAKZKNMDlK3dHBODz4wXNc8cwwHOuDCfqfYh49wZ9ylUcIZIikcGICaYQFWj9NYthPikeoGk8kU20%2BUcxDpTbBuJfXrWEts7YrQ2nUhe64he%2FfnLthSGOsoTDV7THwfR1lJiks6KvAugbI0%2F3nO18FYL8SKeNiV8VgCwN4x%2FzJYkZWdo6EQuB8hjnt0GvlJHXLraDg%2FpXIrznIt4xp6ZH7%2F60F8%2FxwOj5ABSnoz314SI49EwTA7s7tGEacOisyNTSXbudwrZSqFewfOdJus%2BuX3l%2FtR%2Fe6hVf%2FiTci%2BU8VXzH63cvZPXeMvNVThV1jaV2%2BM2CfLNP%2F48Cq%2Fd1I0TtWvWlWvR9WvDq3qqrGTkPWryuk%2FdVnv6A%2Ff0JSPAYFTEnYobPqMVRs%2BHqFpyOugyykL%2Fui%2FxWM8v%2F93yn767izum1EwfePNXiv4GwW%2F8oO5fSh%2BKbT6Hd8Rlr6e%2Fq00bZTgl2ZCv0OL6CMdPYo5K2jQ%2FPb94Qhh3qPCv5EfjVP4N974tRK%2FWeKdQ0t8yd3fERZ%2FxRrOidqKfMfScPVx4jESiynz%2FNbeEbf2Rwd33Vq%2FA0%2BaJ%2FaNnoytVewvDy72%2BnTs4PinYyvWdCMnY8tToc%2FGetBgQCWFjgvs2sW%2BnYLdnJt2DrYmsc%2BF%2FXBi%2F0FnYbcTtVX3jv5UzmMYmvQfkXgB8wY2H8gEHyHYtUt9Oy%2B7OTftxGxdUn9%2BaKlXEwWnIfWNnJotx1V%2FODeN%2FVbqd2PJKUt9uYLpj3Dc137%2FNWgBhHqRZts0q1OC5NUe5HvraqFmXpp3Wf9Q%2Faf8lgUQZdjW9tKUpT%2BLOaUVEDl1G3WxLk%2BF%2Fizlm2989PemfnPZww682Hx5ztfD7ocnlcK9B1HaN6bqkvuylQ%2FvK%2Fcf9JWp7URtxd0qeWkKTfK1D51TeEV2%2F6w4IWmH3eI%2FEjL34n8t7P7%2F)).

## Postman Documentation

Explore the API endpoints and test requests using the Postman documentation available [here](https://documenter.getpostman.com/view/29680874/2sA3BuUoJo).

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
    

5. To run the tests for the API, execute the following command:

    - python manage.py test
