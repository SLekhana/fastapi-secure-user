# FastAPI Secure User Application

A secure user authentication API built with FastAPI, SQLAlchemy, and SQLite.

## Features

- User registration with password hashing (bcrypt)
- User login authentication
- Unique username and email constraints
- Comprehensive unit and integration tests
- CI/CD pipeline with GitHub Actions
- Docker support

## Running Locally

### 1. Clone and Setup
```bash
git clone https://github.com/YOUR-USERNAME/fastapi-secure-user.git
cd fastapi-secure-user
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run Tests
```bash
pytest tests/ -v
```

### 3. Start Application
```bash
uvicorn app.main:app --reload
```

Visit: http://localhost:8000/docs

## API Endpoints

- `POST /users/` - Register new user
- `GET /users/` - List all users
- `GET /users/{id}` - Get user by ID
- `POST /login/` - User login

## Docker
```bash
docker pull YOUR-DOCKERHUB-USERNAME/fastapi-secure-user:latest
docker run -p 8000:8000 YOUR-DOCKERHUB-USERNAME/fastapi-secure-user:latest
```

## Docker Hub

https://hub.docker.com/r/YOUR-DOCKERHUB-USERNAME/fastapi-secure-user

## Author

Lekhana - NJIT Data Sciencey

