# User Management System API
## Live API:
https://mohammedmuk20.pythonanywhere.com/api/

## Overview

The User Management System API allows you to manage user data with endpoints for creating, retrieving, updating, and deleting users. The API supports operations via HTTP methods and handles errors appropriately.


## Endpoints

### 1. Create User

- **Endpoint:** `POST /api/users/create`
- **Description:** Creates a new user.
- **Request:**
  - **Headers:**
    - `Content-Type: application/json`
  - **Body:**
    ```json
    {
      "username": "string"  // The name of the user to be created.
    }
    ```
- **Response:**
  - **Success (201 Created):**
    ```json
    {
      "id": 1,          // Unique identifier for the created user.
      "username": "string"  // The name of the user.
    }
    ```
  - **Error (400 Bad Request):**
    ```json
    {
      "username": ["This field is required."]  // Validation errors if the request is malformed.
    }
    ```

### 2. Retrieve User by Username

- **Endpoint:** `GET /api/users/retrieve`
- **Query Parameters:** `username=name`
- **Description:** Retrieves a user by their username.
- **Request:**
  - **Query Parameter:** `username=name` (Replace `name` with the actual username.)
- **Response:**
  - **Success (200 OK):**
    ```json
    {
      "id": 1,          // Unique identifier of the user.
      "username": "string"  // The name of the user.
    }
    ```
  - **Error (404 Not Found):**
    ```json
    {
      "detail": "Not Found"  // Indicates the user does not exist.
    }
    ```

### 3. Retrieve User by ID

- **Endpoint:** `GET /api/users/retrieve`
- **Query Parameters:** `id=2`
- **Description:** Retrieves a user by their ID.
- **Request:**
  - **Query Parameter:** `id=2` (Replace `2` with the actual user ID.)
- **Response:**
  - **Success (200 OK):**
    ```json
    {
      "id": 2,          // Unique identifier of the user.
      "username": "string"  // The name of the user.
    }
    ```
  - **Error (404 Not Found):**
    ```json
    {
      "detail": "Not Found"  // Indicates the user does not exist.
    }
    ```

### 4. Update User by Username

- **Endpoint:** `PUT /api/users/update`
- **Query Parameters:** `username=name`
- **Description:** Updates the user's information by username.
- **Request:**
  - **Headers:**
    - `Content-Type: application/json`
  - **Query Parameter:** `username=name` (Replace `name` with the current username.)
  - **Body:**
    ```json
    {
      "username": "new_name"  // The new name for the user.
    }
    ```
- **Response:**
  - **Success (200 OK):**
    ```json
    {
      "id": 1,          // Unique identifier of the updated user.
      "username": "new_name"  // The updated name of the user.
    }
    ```
  - **Error (404 Not Found):**
    ```json
    {
      "detail": "Not Found"  // Indicates the user to update does not exist.
    }
    ```
  - **Error (400 Bad Request):**
    ```json
    {
      "username": ["This field is required."]  // Validation errors if the request is malformed.
    }
    ```

### 5. Update User by ID

- **Endpoint:** `PUT /api/users/update`
- **Query Parameters:** `id=2`
- **Description:** Updates the user's information by ID.
- **Request:**
  - **Headers:**
    - `Content-Type: application/json`
  - **Query Parameter:** `id=2` (Replace `2` with the actual user ID.)
  - **Body:**
    ```json
    {
      "username": "new_name"  // The new name for the user.
    }
    ```
- **Response:**
  - **Success (200 OK):**
    ```json
    {
      "id": 2,          // Unique identifier of the updated user.
      "username": "new_name"  // The updated name of the user.
    }
    ```
  - **Error (404 Not Found):**
    ```json
    {
      "detail": "Not Found"  // Indicates the user to update does not exist.
    }
    ```
  - **Error (400 Bad Request):**
    ```json
    {
      "username": ["This field is required."]  // Validation errors if the request is malformed.
    }
    ```

### 6. Delete User by Username

- **Endpoint:** `DELETE /api/users/delete`
- **Query Parameters:** `username=name`
- **Description:** Deletes a user by their username.
- **Request:**
  - **Query Parameter:** `username=name` (Replace `name` with the username of the user to delete.)
- **Response:**
  - **Success (200 OK):**
    ```json
    {
      "success": "User was deleted"  // Validation errors if the request is malformed.
    }
    ```
  - **Error (404 Not Found):**
    ```json
    {
      "detail": "Not Found"  // Indicates the user to delete does not exist.
    }
    ```

### 7. Delete User by ID

- **Endpoint:** `DELETE /api/users/delete`
- **Query Parameters:** `id=2`
- **Description:** Deletes a user by their ID.
- **Request:**
  - **Query Parameter:** `id=2` (Replace `2` with the actual user ID.)
- **Response:**
  - **Success (204 No Content):**
    ```json
    {
      "success": "User was deleted"  // Validation errors if the request is malformed.
    }
    ```
  - **Error (404 Not Found):**
    ```json
    {
      "detail": "Not Found"  // Indicates the user to delete does not exist.
    }
    ```

## Error Handling

The API provides appropriate HTTP status codes and error messages for various scenarios:

- **400 Bad Request:** Returned when the request is invalid or missing required fields. The response will include details about the validation errors.
- **404 Not Found:** Returned when the requested user does not exist. The response will include an error message specifying that the user was not found.

## Example Requests and Responses

### Create User

**Request:**

```bash
curl -X POST http://<your-domain>/api/users/create/ -H "Content-Type: application/json" -d '{"name": "John Doe"}'


## Setup

To set up the project locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**

   ```bash
   pip install django djangorestframework

4. **Apply Migrations**

   ```bash
   python manage.py migrate

5. **Run the Development Server**

   ```bash
   python manage.py runserver
