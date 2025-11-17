import pytest
from fastapi import status


class TestUserRegistration:
    """Integration tests for user registration"""
    
    def test_register_user_success(self, client):
        """Test successful user registration"""
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "securepass123"
        }
        
        response = client.post("/users/", json=user_data)
        
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["username"] == "testuser"
        assert data["email"] == "test@example.com"
        assert "password" not in data
        assert "password_hash" not in data
        assert "id" in data
        assert "created_at" in data
    
    def test_register_duplicate_username(self, client):
        """Test registration with duplicate username"""
        user_data = {
            "username": "testuser",
            "email": "test1@example.com",
            "password": "securepass123"
        }
        
        # Create first user
        response1 = client.post("/users/", json=user_data)
        assert response1.status_code == status.HTTP_201_CREATED
        
        # Try to create user with same username but different email
        user_data["email"] = "test2@example.com"
        response2 = client.post("/users/", json=user_data)
        
        assert response2.status_code == status.HTTP_400_BAD_REQUEST
        assert "username already registered" in response2.json()["detail"].lower()
    
    def test_register_duplicate_email(self, client):
        """Test registration with duplicate email"""
        user_data1 = {
            "username": "testuser1",
            "email": "test@example.com",
            "password": "securepass123"
        }
        
        # Create first user
        response1 = client.post("/users/", json=user_data1)
        assert response1.status_code == status.HTTP_201_CREATED
        
        # Try to create user with different username but same email
        user_data2 = {
            "username": "testuser2",
            "email": "test@example.com",
            "password": "securepass456"
        }
        response2 = client.post("/users/", json=user_data2)
        
        assert response2.status_code == status.HTTP_400_BAD_REQUEST
        assert "email already registered" in response2.json()["detail"].lower()
    
    def test_register_invalid_email(self, client):
        """Test registration with invalid email format"""
        user_data = {
            "username": "testuser",
            "email": "not-an-email",
            "password": "securepass123"
        }
        
        response = client.post("/users/", json=user_data)
        
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    def test_register_short_password(self, client):
        """Test registration with too short password"""
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "short"
        }
        
        response = client.post("/users/", json=user_data)
        
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    def test_register_short_username(self, client):
        """Test registration with too short username"""
        user_data = {
            "username": "ab",
            "email": "test@example.com",
            "password": "securepass123"
        }
        
        response = client.post("/users/", json=user_data)
        
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


class TestUserRetrieval:
    """Integration tests for user retrieval"""
    
    def test_get_users_empty(self, client):
        """Test getting users when database is empty"""
        response = client.get("/users/")
        
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []
    
    def test_get_users_list(self, client):
        """Test getting list of users"""
        # Create multiple users
        users = [
            {"username": "user1", "email": "user1@example.com", "password": "password123"},
            {"username": "user2", "email": "user2@example.com", "password": "password123"},
            {"username": "user3", "email": "user3@example.com", "password": "password123"}
        ]
        
        for user in users:
            client.post("/users/", json=user)
        
        response = client.get("/users/")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data) == 3
        assert all("password" not in user for user in data)
        assert all("password_hash" not in user for user in data)
    
    def test_get_user_by_id(self, client):
        """Test getting a specific user by ID"""
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "securepass123"
        }
        
        # Create user
        create_response = client.post("/users/", json=user_data)
        user_id = create_response.json()["id"]
        
        # Get user by ID
        response = client.get(f"/users/{user_id}")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == user_id
        assert data["username"] == "testuser"
        assert "password" not in data
        assert "password_hash" not in data
    
    def test_get_user_not_found(self, client):
        """Test getting a user that doesn't exist"""
        response = client.get("/users/999")
        
        assert response.status_code == status.HTTP_404_NOT_FOUND


class TestUserLogin:
    """Integration tests for user login"""
    
    def test_login_success(self, client):
        """Test successful login"""
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "securepass123"
        }
        
        # Register user
        client.post("/users/", json=user_data)
        
        # Login
        login_data = {
            "username": "testuser",
            "password": "securepass123"
        }
        response = client.post("/login/", json=login_data)
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "message" in data
        assert data["username"] == "testuser"
        assert "user_id" in data
    
    def test_login_wrong_password(self, client):
        """Test login with wrong password"""
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "securepass123"
        }
        
        # Register user
        client.post("/users/", json=user_data)
        
        # Login with wrong password
        login_data = {
            "username": "testuser",
            "password": "wrongpassword"
        }
        response = client.post("/login/", json=login_data)
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_login_nonexistent_user(self, client):
        """Test login with non-existent username"""
        login_data = {
            "username": "nonexistent",
            "password": "password123"
        }
        response = client.post("/login/", json=login_data)
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestRootEndpoints:
    """Integration tests for root and health endpoints"""
    
    def test_root_endpoint(self, client):
        """Test root endpoint"""
        response = client.get("/")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "message" in data
        assert "version" in data
    
    def test_health_check(self, client):
        """Test health check endpoint"""
        response = client.get("/health")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["status"] == "healthy"
