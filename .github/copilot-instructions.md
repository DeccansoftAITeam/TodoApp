# GitHub Copilot Custom Instructions

## Project Overview
This is an enterprise-grade application with:
- **Backend**: Python (FastAPI/Django/Flask) with RESTful APIs
- **Frontend**: React with modern JavaScript/TypeScript
- **Architecture**: Separated concerns with Backend and Frontend folders in the same workspace

---

## General Development Standards

### Code Quality
- Follow SOLID principles and clean code practices
- Write self-documenting code with meaningful variable and function names
- Prioritize readability and maintainability over cleverness
- Include comprehensive error handling and logging
- Add type hints/annotations wherever applicable

### Documentation
- Generate clear docstrings for all functions, classes, and modules
- Include usage examples in complex function documentation
- Document API endpoints with request/response examples
- Keep README files updated with setup and deployment instructions

### Testing
- Write unit tests for all business logic
- Include integration tests for API endpoints
- Maintain minimum 80% code coverage
- Follow AAA pattern (Arrange, Act, Assert) in tests

---

## Python Backend Standards

### Framework Conventions
- Use FastAPI for async APIs, Flask for simpler services, Django for full-stack needs
- Organize code: `/routes`, `/services`, `/models`, `/utils`, `/middleware`
- Implement dependency injection for services and repositories
- Use Pydantic models for request/response validation

### Python Best Practices
- Follow PEP 8 style guide
- Use type hints for all function parameters and return types
- Prefer async/await for I/O operations
- Use dataclasses or Pydantic models for data structures
- Implement proper exception handling with custom exception classes

### Database Operations
- Use SQLAlchemy ORM or async alternatives (Tortoise ORM, SQLModel)
- Always use parameterized queries to prevent SQL injection
- Implement database migrations (Alembic for SQLAlchemy)
- Create repository pattern for data access layer
- Use connection pooling for production environments

### API Design
- Follow RESTful conventions (GET, POST, PUT, DELETE, PATCH)
- Use proper HTTP status codes (200, 201, 400, 401, 404, 500)
- Implement pagination for list endpoints
- Version APIs using URL prefix (/api/v1/)
- Include CORS configuration for frontend integration

### Security
- Implement JWT or OAuth2 authentication
- Use environment variables for sensitive data (never hardcode secrets)
- Validate and sanitize all user inputs
- Implement rate limiting for API endpoints
- Use HTTPS in production environments

### Code Example Format
python
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

router = APIRouter(prefix="/api/v1/items", tags=["items"])

@router.get("/", response_model=List[ItemResponse])
async def get_items(skip: int = 0, limit: int = 100):
    """Retrieve paginated list of items."""
    # Implementation
    pass

---

## React Frontend Standards

### Project Structure
- Organize by feature: `/components`, `/pages`, `/hooks`, `/services`, `/utils`, `/context`
- Keep components small and focused (Single Responsibility)
- Separate presentational and container components
- Use index files for clean imports

### Component Development
- Use functional components with hooks (avoid class components)
- Implement proper prop validation with PropTypes or TypeScript
- Extract reusable logic into custom hooks
- Use React.memo for expensive render operations
- Implement error boundaries for component error handling

### State Management
- Use Context API for global state or Redux/Zustand for complex state
- Keep state as local as possible
- Use useReducer for complex state logic
- Implement proper loading and error states
- Cache API responses appropriately

### API Integration
- Create a centralized API service layer using axios or fetch
- Implement request/response interceptors for auth tokens
- Use React Query or SWR for data fetching and caching
- Handle loading, error, and success states consistently
- Implement retry logic for failed requests

### Styling Standards
- Use CSS Modules, Styled Components, or Tailwind CSS consistently
- Follow mobile-first responsive design
- Implement theme variables for colors, spacing, typography
- Ensure accessibility (ARIA labels, semantic HTML, keyboard navigation)
- Use CSS-in-JS or preprocessors (SASS/LESS) for complex styling

### Performance Optimization
- Implement code splitting with React.lazy and Suspense
- Optimize images (use WebP, lazy loading)
- Memoize expensive computations with useMemo
- Debounce/throttle user input handlers
- Use production builds for deployment

### Code Example Format
jsx
import React, { useState, useEffect } from 'react';
import { apiService } from '../services/api';

interface Item {
  id: number;
  name: string;
  description?: string;
}

export const ItemList: React.FC = () => {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchItems();
  }, []);

  const fetchItems = async () => {
    try {
      const data = await apiService.getItems();
      setItems(data);
    } catch (err) {
      setError('Failed to fetch items');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return Loading...;
  if (error) return Error: {error};

  return (
    
      {items.map(item => (
        {item.name}
      ))}
    
  );
};

---

## Integration Standards

### API Communication
- Backend serves at `/api/v1/*` endpoints
- Frontend uses environment variables for API base URL
- Implement proper CORS headers on backend
- Use consistent error response format across all endpoints
- Include request/response logging for debugging

### Authentication Flow
- Backend issues JWT tokens on successful login
- Frontend stores tokens securely (httpOnly cookies preferred)
- Include Authorization header in all authenticated requests
- Implement token refresh mechanism
- Handle 401 responses with automatic logout

### Error Handling
- Backend returns structured error responses with error codes
- Frontend displays user-friendly error messages
- Log errors to monitoring service (Sentry, LogRocket)
- Implement retry logic for transient failures
- Show appropriate fallback UI for errors

---

## Development Workflow

### Git Practices
- Use feature branches with descriptive names
- Write clear, conventional commit messages
- Keep commits atomic and focused
- Review code before merging (PR/MR process)
- Maintain clean commit history

### Code Generation Preferences
- Generate complete, production-ready code
- Include error handling in all generated code
- Add comments for complex logic only
- Suggest improvements and optimizations
- Follow the principle: decision training, not tool training

### When Suggesting Code
- Explain the reasoning behind architectural decisions
- Highlight potential edge cases and gotchas
- Suggest alternative approaches when applicable
- Reference relevant documentation or best practices
- Consider scalability and maintainability

---

## Enterprise Considerations

### Scalability
- Design for horizontal scaling
- Implement caching strategies (Redis)
- Use message queues for async operations (RabbitMQ, Celery)
- Optimize database queries with indexes
- Implement connection pooling and resource management

### Monitoring & Observability
- Add structured logging with correlation IDs
- Implement health check endpoints
- Use APM tools (New Relic, DataDog)
- Track key business metrics
- Set up alerting for critical failures

### Security Compliance
- Follow OWASP Top 10 security practices
- Implement input validation and output encoding
- Use security headers (CSP, HSTS, X-Frame-Options)
- Regular dependency updates and vulnerability scanning
- Conduct security reviews for sensitive operations

### Deployment
- Use containerization (Docker) for consistency
- Implement CI/CD pipelines
- Maintain separate dev, staging, production environments
- Use environment-specific configurations
- Implement database migration strategies

---

## AI-Assisted Development Notes

When using GitHub Copilot:
- Review all generated code before accepting
- Verify security implications of generated code
- Test generated code thoroughly
- Refactor generated code to match team standards
- Use Copilot as a pair programmer, not a replacement for thinking