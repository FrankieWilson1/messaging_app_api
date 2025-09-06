# API Documentation

## Base URL
```
https://frankiewilson.pythonanywhere.com/api/v1/
```

## Authentication
The API endpoints are protected using JWT (JSON Web Token) authentication. You must obtain a token before accessing most endpoints. 

### Authentication Endpoints
| Method | Endpoint               | Description                                   |
|--------|-----------------------|-----------------------------------------------|
| POST   | /api/v1/register/     | Create a new user account.                   |
| POST   | /api/v1/token/        | Obtain an access token and a refresh token.  |
| POST   | /api/v1/token/refresh/| Refresh an expired access token using the refresh token. |

**Example: Get Access Token**

**Request Body:**
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

### Example Usage:
```bash
curl -X POST https://frankiewilson.pythonanywhere.com/api/v1/token/ \
-H "Content-Type: application/json" \
-d '{"username": "your_username", "password": "your_password"}'
```

## Protected Endpoints
All requests to the following endpoints require a valid access token in the `Authorization: Bearer <token>` header.

### User Endpoints
| Method | Endpoint                  | Description                          |
|--------|---------------------------|--------------------------------------|
| GET    | /api/v1/users/            | List all users.                     |
| GET    | /api/v1/users/<user_id>/   | Retrieve a specific user by ID.    |

### Example Usage:
```bash
curl -X GET https://frankiewilson.pythonanywhere.com/api/v1/users/ \
-H "Authorization: Bearer <your_access_token>"
```

### Conversation Endpoints
| Method | Endpoint                       | Description                                          |
|--------|--------------------------------|------------------------------------------------------|
| POST   | /api/v1/conversations/         | Create a new conversation with a list of user IDs. |
| GET    | /api/v1/conversations/         | List all conversations the authenticated user is a participant of. |

### Example Usage (Create a Conversation):
```bash
curl -X POST https://frankiewilson.pythonanywhere.com/api/v1/conversations/ \
-H "Authorization: Bearer <your_access_token>" \
-H "Content-Type: application/json" \
-d '{"user_ids": [1, 2, 3]}'
```

### Message Endpoints
| Method | Endpoint                            | Description                                   |
|--------|-------------------------------------|-----------------------------------------------|
| POST   | /api/v1/conversations/<conv_id>/messages/ | Send a new message to a specific conversation. |
| GET    | /api/v1/conversations/<conv_id>/messages/ | List all messages in a specific conversation. |

### Example Usage (Send a Message):
```bash
curl -X POST https://frankiewilson.pythonanywhere.com/api/v1/conversations/<conv_id>/messages/ \
-H "Authorization: Bearer <your_access_token>" \
-H "Content-Type: application/json" \
-d '{"message": "Hello, this is a test message."}'
```

## Usage
You can test the API endpoints using the following methods:

- **Web Browser:** Access `http://localhost:8000/register/` to use a simple register page to register befor accessings. You can also view a browsable API at `http://localhost:8000/api/v1/` for GET requests.
- **cURL:** Use curl commands in your terminal as demonstrated in our previous discussions.
- **Postman/Insomnia (recomendend):** These tools provide a user-friendly interface for sending and managing API requests.
