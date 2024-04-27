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


![Library ERD](https://github.com/F0laf0lu/LibraryApi/assets/119736310/63bbe5c2-a74e-4822-a71c-1d1a9e3fd7bb)

For the database schema, refer to the [Entity Relationship Diagram (ERD)](https://app.diagrams.net/?title=Library%20ERD.drawio#R7VxRc6I6FP41zOx92A5Cse1jpbq7c%2B3eTte9d2ZfOilEzC0mTIhV99fvCQQQAYutVgvOOA4cjifJ%2Bb7ziSRRM%2B3p4gtHweSWudjXDN1daOaNZhiX3Ut4l4ZlbLD089jgceLGpk5m%2BEF%2BY2XUlXVGXBzmHAVjviBB3ugwSrEjcjbEOZvn3cbMz7caIA8XDD8c5Bet%2FxFXTNSwLD2zf8XEmyQtd3R1ZYoSZ2UIJ8hl85wJL8SAUaG6eIf5FFFMBVy5RfwJc83qT4SQI73WjAG8xtL7zGPM8zEKSHjmsCmYnRBcBmM0Jb5M80qgngoEzZl9zbQ5YyI%2Bmi5s7EuoEhjiPg0qrqZ54DJujQ%2FYn5%2BXwydd0K9z819xe%2BvdXTx%2BVlGekT9T%2BVW5Ecsk4diF%2FKtTaIqI5T32kSCM9rMrPUzda4kuOPXvf2PORuwWURh8LxSIi%2Bwao8p9QKB75k0ncVHnOpwXh6b6GbIZd%2FCG8RiKzBDQw2KDY1cB7ubYpjL3BbMpFnwJDvOMYymTJqv8Sow8SspznqVIMclLA6Zt3DESEUvVpXmu4qiyvEgomYSIh64%2BtQrzWqDztUDd9UBxagqB4GBl4JkpYtEWjDIKjOox9lRgFRRfIA8Feoz4E1FAqY0pOQD6IRChUCoxRxzm%2BygISeQeWybEd4doyWYiCZSc9cZkgd37WGykL7BvCMFCRTBZtgmn5WXkE4%2FCsQOEky32OA6hL0MUCuVRSclnzAVebORQgoxl5JDpJMiscCyV2VWOGRd6NZ1y%2BG0Llvly%2BSdAwdAFQf49aDqiXoRZHhKZV5ezYJSUnjQEkmaY959xrKpR8qHQbeYziSyN5SByiwZn9eAFw7X1M0uzoAM2nHeyc3hJdy5sRkPBEYngwADUHEuweoIFqh0fj5NucJVMefzIhACRroJ1I6lfxlpha9aE1twXsucFZO%2F%2B3gZbBmMd%2B5FmT4jrYhqXpPxKRxneJVCW5j%2FN%2BToY64VYEw%2BzNh4rAJhb5l8Fy7KydTTkA%2FcpErjHZtQN9yG3VgHnx0hu5adsQ7uGHunf%2FxnJ95%2FD4REyIJHe2LcXBsgh1BvGn%2ByuUcTaB0UWWlXJdi53Spla4d6BM902q375%2FeVuVL97aNW%2FeBOy71TxNbPfrZ39pmv8ZQFV%2BBUW9dWZIP7J0PW%2FPrzK75wUrVP1q5Oq70fVrw6t6kljjZD1q9rpb7qsd4oP39BMTACBJgk7FDZ7wkkbLh6jmS%2F2QZcmC%2F74%2F%2BVDsLj%2FNeM%2FXXse9HXqzd54s9cYwS9Qo%2B53QKXg134wtwvFL4W2eMd3hKVfK%2F3VzG204JcOu3iHRtkDGz%2FIOStoUP%2F2fXSEML9R4XfIj9Yp%2FBtv%2FE4SXy3x1qElvuTu7wiL%2F%2FU1HCezfSLfMQq4ujh0OAnklHl6a2%2FJW%2Fujg%2FsAWl%2FFk%2FaJfasnY%2Fcq9pcHF%2FvidOzg%2BKdjX1%2FTZku1vzgb60CDHlMUOi6wDyH2FcRon9if5mD3JPapsB9O7D%2FQLOyrirjbUnUvPpVzOIYm3QckF2DewOGITPERgn0Iqa9gSfuk%2FjQxuy%2BpPz%2B01CcTBY2V%2Bqt2Sr1RfDg3C9yT1G%2FHkiZLfblcFR%2Fh2C%2F9%2FmvRBohkIc2maVarBMmrHcj3xt1C7fxq3mb%2FQ%2F3V1Bs2QJRhu7dFU0bxWUyTdkCk1D2tozKKz1K%2BudpHXzf1ym0PW%2FCi%2Bus53Q%2B7G57UCvceRDmtmNqX3JftfHhfuf9AS6Zezv9F7fw3XtxLFk2habr3odOEJbK7Z0WDpB1Os%2F9IiN2z%2F7Uw%2B38A).

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
