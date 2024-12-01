# Simple api rest with Django and Django-restframework
## Summary
This project is a simple API REST for managing movies, built with Django and Django REST framework. It allows users to perform CRUD operations on movie data, including creating, reading, updating, and deleting movie records.

## How to Deploy with Poetry
1. **Install Poetry**: If you haven't already, install Poetry by following the instructions at [Poetry's official website](https://python-poetry.org/docs/#installation).
2. **Install Dependencies**: Navigate to the project directory and run:
    ```bash
    poetry install
    ```
3. **Run Migrations**: Apply the database migrations with:
    ```bash
    poetry run poe migrate
    ```
4. **Start the Server**: Launch the development server using:
    ```bash
    poetry run poe runserver
    ```

## Endpoints
- **POST /auth/token/**: Obtain a new authentication token.
- **POST /auth/token/refresh/**: Refresh an existing authentication token.
- **POST /auth/register/**: Register a new user.
- **GET /movies/**: Retrieve a list of all movies.
- **POST /movies/**: Create a new movie.
- **GET /movies/{id}/**: Retrieve details of a specific movie by ID.
- **PUT /movies/{id}/**: Update an existing movie by ID.
- **DELETE /movies/{id}/**: Delete a movie by ID.

## API Documentation with Swagger
This project includes Swagger for API documentation. Swagger provides a user-friendly interface to interact with the API endpoints and view the available operations.

### Accessing Swagger UI
To access the Swagger UI, follow these steps:
1. **Start the Server**: Ensure the development server is running:
    ```bash
    poetry run poe runserver
    ```
2. **Open Swagger UI**: Navigate to `http://localhost:8000/api/v1/swagger/` in your web browser to view the API documentation.

## Additional Endpoint
- **GET /swagger/**: Access the Swagger UI for API documentation.
- **GET /redoc/**: Regenerate the Swagger Docs for API documentation.