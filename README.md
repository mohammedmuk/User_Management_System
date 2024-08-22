# User Management System API
## Live API:
https://mohammedmuk20.pythonanywhere.com/api/

## Overview

The User Management System API allows you to manage user data with endpoints for creating, retrieving, updating, and deleting users. The API supports operations via HTTP methods and handles errors appropriately.

## Endpoints

### 1. Create User

- **Endpoint:** `POST /api/users/create/`
- **Description:** Creates a new user.
- **Request:**
  ```json
  {
    "name": "string"  // The name of the user to be created.
  }

- **Response:**
-   **Success (201 created)
