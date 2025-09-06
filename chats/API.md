# Messaging App API

This is a RESTful API for a messaging application, built with Django and Django REST Framework. The project uses Docker for containerization, ensuring a consistent development environment.

## 1. Project Setup

This project uses docker-compose to manage the application and its services (a Django web server and a MySQL database).

### Prerequisites
- **Docker**: Install Docker on your system.
- **Docker Compose**: This is typically included with Docker Desktop. If not, you can install it separately.

### Running the Project
1. **Build the Docker Image**: Navigate to the root of the project directory and build the Docker image for the web service.
   ```bash
   docker-compose build web
   ```
2. **Start the Services**: Launch the web and database containers. The `-d` flag runs the services in the background.
   ```bash
   docker-compose up -d
   ```
3. **Run Database Migrations**: The `entrypoint.sh` script handles initial migrations automatically on startup. If you need to run migrations manually after making model changes, you can do so with these commands:
   ```bash
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   ```
4. **Create a Superuser**: To access the admin panel and create a test user for your API, run:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

## 2. API Endpoints

The API endpoints are protected using JWT (JSON Web Token) authentication. You must obtain a token before accessing most endpoints. All API endpoints are prefixed with `/api/v1/`.

### Authentication

| Method | Endpoint               | Description                         |
|--------|------------------------|-------------------------------------|
| POST   | /api/v1/register/      | Create a new user account.         |
| POST   | /api/v1/token/         | Obtain an access token and a refresh token. |
| POST   | /api/v1/token/refresh/ | Refresh an expired access token using the refresh token. |

#### Example: Get Access Token
**Request Body:**
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

### Protected Endpoints

All requests to these endpoints require a valid access token in the `Authorization: Bearer <token>` header.

#### User Endpoints

| Method | Endpoint                  | Description                             |
|--------|---------------------------|-----------------------------------------|
| GET    | /api/v1/users/            | List all users.                        |
| GET    | /api/v1/users/<user_id>/   | Retrieve a specific user by ID.       |

#### Conversation Endpoints

| Method | Endpoint                     | Description                                   |
|--------|------------------------------|-----------------------------------------------|
| POST   | /api/v1/conversations/        | Create a new conversation with a list of user IDs. |
| GET    | /api/v1/conversations/       | List all conversations the authenticated user is a participant of. |

#### Message Endpoints

| Method | Endpoint                                   | Description                          |
|--------|--------------------------------------------|--------------------------------------|
| POST   | /api/v1/conversations/<conv_id>/messages/ | Send a new message to a specific conversation. |
| GET    | /api/v1/conversations/<conv_id>/messages/ | List all messages in a specific conversation. |

## 3. Usage

You can test the API endpoints using the following methods:
- **Web Browser**: Access `http://localhost:8000/login/` to use a simple login page that retrieves your tokens. You can also view a browsable API at `http://localhost:8000/api/v1/` for GET requests.
- **cURL**: Use curl commands in your terminal as demonstrated in our previous discussions.
- **Postman/Insomnia**: These tools provide a user-friendly interface for sending and managing API requests.
