# Assignment Reflection Document

**Student Name**: Lekhana  
**Course**: DS677 - Deep Learning  
**Assignment**: Secure User Model with FastAPI and CI/CD Pipeline  
**Date**: November 17, 2025

---

## 1. Overview

This project implements a secure user authentication system using FastAPI, SQLAlchemy, and SQLite/PostgreSQL. The application includes password hashing with bcrypt, comprehensive testing with pytest, and automated CI/CD deployment to Docker Hub via GitHub Actions.

---

## 2. Key Learnings

### Technical Skills Developed

1. **FastAPI Development**
   - Built RESTful API endpoints for user registration, login, and retrieval
   - Implemented request/response validation with Pydantic schemas
   - Used dependency injection for database sessions

2. **Database Management**
   - Created SQLAlchemy ORM models with unique constraints
   - Managed database sessions and transactions
   - Worked with both SQLite (local) and PostgreSQL (CI/CD)

3. **Security Best Practices**
   - Implemented password hashing using bcrypt
   - Never stored plain-text passwords
   - Excluded sensitive data from API responses

4. **Testing**
   - Wrote 25 unit and integration tests
   - Used pytest fixtures for test isolation
   - Achieved high test coverage

5. **DevOps & CI/CD**
   - Set up GitHub Actions workflow
   - Configured PostgreSQL service container for tests
   - Built and pushed Docker images automatically

---

## 3. Challenges Faced and Solutions

### Challenge 1: Password Hashing Compatibility
**Problem**: The passlib library had compatibility issues with the newer bcrypt version on Python 3.13, causing ValueError during password hashing.

**Solution**: Switched from passlib to using bcrypt directly, implementing hash_password() and verify_password() functions with bcrypt.hashpw() and bcrypt.checkpw().

**Learning**: Library compatibility can vary across Python versions. Reading error messages carefully and understanding the underlying issue helps find alternative solutions.

### Challenge 2: PostgreSQL Driver in CI/CD
**Problem**: The psycopg2-binary package failed to build on Mac locally but was required for PostgreSQL tests in GitHub Actions.

**Solution**: Kept psycopg2-binary in requirements.txt for CI/CD (works on Linux), while local development uses SQLite which doesn't require it.

**Learning**: Different environments may have different dependencies. The CI/CD pipeline runs on Linux where binary packages install cleanly.

### Challenge 3: Docker Hub Authentication
**Problem**: GitHub Actions failed with "unauthorized: incorrect username or password" when trying to push to Docker Hub.

**Solution**: Created a new Docker Hub access token with proper permissions and carefully re-added the secrets to GitHub repository settings.

**Learning**: Access tokens are more secure than passwords and must be copied immediately as they're only shown once.

---

## 4. Development Process

### Initial Setup
Set up the project structure with separate directories for app code and tests. Created virtual environment and installed dependencies. Used nano editor in terminal for all file creation.

### Implementation
Started with database models and schemas, then implemented authentication functions, CRUD operations, and finally the FastAPI endpoints. Each component was built incrementally and tested.

### Testing
Wrote unit tests for password hashing and schema validation first, then integration tests for all API endpoints. Used pytest fixtures to ensure database isolation between tests.

### CI/CD Configuration
Created GitHub Actions workflow with two jobs: testing (with PostgreSQL service) and Docker deployment. Configured secrets for Docker Hub authentication.

---

## 5. Testing Results

### Local Testing
- Total Tests: 25
- Passed: 25
- Failed: 0
- Coverage: ~95%

### CI/CD Testing
- All tests passed in GitHub Actions: Yes
- PostgreSQL integration tests: Yes
- Docker image built successfully: Yes
- Docker image pushed to Docker Hub: Yes

---

## 6. Project Deliverables

### GitHub Repository
- URL: https://github.com/SLekhana/fastapi-secure-user
- Contains all source code, tests, and CI/CD configuration

### Docker Hub
- Image: slekhana/fastapi-secure-user:latest
- Successfully deployed via GitHub Actions

---

## 7. Code Quality

### Best Practices Implemented
- [x] Proper code organization (app/, tests/)
- [x] Clear function and variable naming
- [x] Docstrings for functions
- [x] Error handling with HTTPException
- [x] Input validation with Pydantic
- [x] Password hashing (never store plain text)
- [x] Test coverage > 90%

### Areas for Improvement
- Add JWT token authentication for stateless sessions
- Implement user update and delete endpoints
- Add database migrations with Alembic
- Add rate limiting for login attempts

---

## 8. Future Enhancements

If I were to continue this project, I would add:

1. JWT token-based authentication for better security
2. Password reset functionality with email verification
3. Role-based access control (admin, user)
4. API rate limiting to prevent abuse
5. Logging and monitoring integration

---

## 9. Time Investment

- Project setup: 1 hour
- Implementation: 2 hours
- Testing: 1 hour
- CI/CD configuration: 1.5 hours
- Debugging: 1 hour
- Documentation: 0.5 hours
- **Total**: ~7 hours

---

## 10. Conclusion

### Overall Experience
This assignment provided hands-on experience with modern API development practices. Building a complete CI/CD pipeline from scratch was particularly valuable, as it demonstrates the full software development lifecycle from code to deployment.

### Key Takeaways
1. Automated testing catches bugs early and ensures code quality
2. CI/CD pipelines save time and reduce deployment errors
3. Security should be built-in from the start, not added later
4. Good documentation helps others (and future self) understand the project

### Confidence Level
On a scale of 1-10:
- Building REST APIs: 8/10
- Database management: 7/10
- Writing tests: 8/10
- CI/CD pipelines: 7/10
- Docker: 7/10

---

## 11. References

- FastAPI Documentation: https://fastapi.tiangolo.com
- SQLAlchemy Documentation: https://docs.sqlalchemy.org
- Pytest Documentation: https://docs.pytest.org
- GitHub Actions Documentation: https://docs.github.com/en/actions
- Docker Documentation: https://docs.docker.com

---

**Submission Date**: November 17, 2025  
**GitHub Repository**: https://github.com/SLekhana/fastapi-secure-user  
**Docker Hub**: https://hub.docker.com/r/slekhana/fastapi-secure-user
