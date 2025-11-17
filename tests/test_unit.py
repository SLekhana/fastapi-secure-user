import pytest
from app.auth import hash_password, verify_password
from app.schemas import UserCreate, UserRead
from pydantic import ValidationError
from datetime import datetime


class TestPasswordHashing:
    """Unit tests for password hashing functions"""
    
    def test_hash_password(self):
        """Test that password hashing works"""
        password = "securepassword123"
        hashed = hash_password(password)
        
        assert hashed is not None
        assert hashed != password
        assert len(hashed) > 0
    
    def test_hash_password_different_each_time(self):
        """Test that same password produces different hashes (salt)"""
        password = "securepassword123"
        hash1 = hash_password(password)
        hash2 = hash_password(password)
        
        assert hash1 != hash2
    
    def test_verify_password_correct(self):
        """Test password verification with correct password"""
        password = "securepassword123"
        hashed = hash_password(password)
        
        assert verify_password(password, hashed) is True
    
    def test_verify_password_incorrect(self):
        """Test password verification with incorrect password"""
        password = "securepassword123"
        wrong_password = "wrongpassword"
        hashed = hash_password(password)
        
        assert verify_password(wrong_password, hashed) is False
    
    def test_verify_password_empty(self):
        """Test password verification with empty password"""
        password = "securepassword123"
        hashed = hash_password(password)
        
        assert verify_password("", hashed) is False


class TestUserSchemas:
    """Unit tests for Pydantic schemas"""
    
    def test_user_create_valid(self):
        """Test UserCreate schema with valid data"""
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "securepass123"
        }
        user = UserCreate(**user_data)
        
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.password == "securepass123"
    
    def test_user_create_invalid_email(self):
        """Test UserCreate schema with invalid email"""
        user_data = {
            "username": "testuser",
            "email": "not-an-email",
            "password": "securepass123"
        }
        
        with pytest.raises(ValidationError) as exc_info:
            UserCreate(**user_data)
        
        errors = exc_info.value.errors()
        assert any(error["type"] == "value_error" for error in errors)
    
    def test_user_create_short_username(self):
        """Test UserCreate schema with too short username"""
        user_data = {
            "username": "ab",
            "email": "test@example.com",
            "password": "securepass123"
        }
        
        with pytest.raises(ValidationError):
            UserCreate(**user_data)
    
    def test_user_create_short_password(self):
        """Test UserCreate schema with too short password"""
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "short"
        }
        
        with pytest.raises(ValidationError):
            UserCreate(**user_data)
    
    def test_user_read_schema(self):
        """Test UserRead schema"""
        user_data = {
            "id": 1,
            "username": "testuser",
            "email": "test@example.com",
            "created_at": datetime.now()
        }
        user = UserRead(**user_data)
        
        assert user.id == 1
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert isinstance(user.created_at, datetime)
