# Messaging Application API

## Project Overview
This project is a backend API for a real-time messaging application, built with Django REST Framework. It provides a secure and scalable foundation for managing users, conversations, and messages. This README.md serves as a high-level overview, while comprehensive, browsable documentation is available at a separate URL.

## 🚀 Features
- **User, Conversation, and Message Management**: The API offers a full suite of endpoints for managing core messaging resources.
- **Django REST Framework**: Built on a solid, well-documented framework to ensure a robust and maintainable codebase.
- **Secure Authentication**: User authentication is handled using JSON Web Tokens (JWT), providing secure access to protected endpoints.
- **Comprehensive Documentation**: The entire API is self-documented and accessible via a browsable web interface, making it easy for developers to get started.

## 🛠️ Technologies Used
- Python 3.x
- Django 5.x
- Django REST Framework 3.x
- MySQL (for the database)

## 📦 Getting Started

### Prerequisites
Make sure you have Python 3.x and a MySQL database instance ready.

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/FrankieWilson1/alx-backend-python
   cd alx-backend-python/messaging_app
   ```

2. **Configure Environment Variables**:
   Create a `.env` file in the `messaging_app` directory to store your database credentials and Django secret key.
   ```plaintext
   # .env
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=127.0.0.1
   DB_PORT=3306
   ```

3. **Install Dependencies**:
   It's highly recommended to use a virtual environment.
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   Apply the database migrations to set up your database schema.
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## 🖥️ Running the Application
To run the application locally, use the Django development server:
```bash
python manage.py runserver
```
The API will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## 📄 API Documentation
Full, browsable API documentation is available at the root URL of your running application. This includes detailed information on every endpoint, request bodies, response formats, and status codes.
- **Full Documentation URL**: [Documentation](https://frankiewilson.pythonanywhere.com/)

## 🤝 Contribution
Contributions are welcome! If you find a bug or want to add a feature, please create a Pull Request with a clear description of the changes.

## Endpoints Summary
This is a quick reference for the main API endpoints. For full details, please refer to the **[Documentation](https://frankiewilson.pythonanywhere.com/docs/)**.

### Base URL: https://frankiewilson.pythonanywhere.com/docs/

### Authentication Endpoints
| Method | Endpoint          |
|--------|-------------------|
| POST   | /register/        |
| POST   | /token/           |
| POST   | /token/refresh/   |

### User Endpoints
| Method | Endpoint      |
|--------|---------------|
| GET    | /users/me/    |
| PATCH  | /users/me/    |
| DELETE | /users/me/    |

### Conversation Endpoints
| Method | Endpoint          |
|--------|-------------------|
| POST   | /conversations/    |
| GET    | /conversations/    |

### Message Endpoints
| Method | Endpoint                                  |
|--------|-------------------------------------------|
| POST   | /conversations/<uuid:conversation_id>/messages/ |
| GET    | /conversations/<uuid:conversation_id>/messages/ |
