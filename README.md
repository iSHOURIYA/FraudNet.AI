# FraudNet.AI - Real-Time Fraud Detection Pipeline

[![CI/CD](https://github.com/your-username/fraudnet-ai/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/your-username/fraudnet-ai/actions/workflows/ci-cd.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

A production-ready, enterprise-grade fraud detection system built with Flask, scikit-learn, and modern MLOps practices. FraudNet.AI provides real-time transaction analysis, machine learning-based fraud prediction, and comprehensive audit trails.

## 🚀 Features

### Core Functionality
- **Real-time Fraud Detection**: Sub-200ms transaction processing with ML-based risk assessment
- **Feature Engineering Pipeline**: Training-inference parity with automated feature extraction
- **Model Management**: Versioned model registry with automated retraining capabilities
- **REST API**: Comprehensive API for transaction processing and system management
- **Audit Trail**: Immutable logging with cryptographic integrity verification

### Security & Production Readiness
- **API Key Authentication**: Secure access control with permission-based authorization
- **Rate Limiting**: Token bucket algorithm with Redis backend
- **Input Validation**: Comprehensive request validation and sanitization
- **Security Headers**: OWASP-compliant security headers and CORS configuration
- **Docker Support**: Multi-stage builds with security hardening
- **CI/CD Pipeline**: Automated testing, security scanning, and deployment

### Monitoring & Observability
- **Structured Logging**: JSON-formatted logs with correlation IDs
- **Health Checks**: Comprehensive system health monitoring
- **Performance Metrics**: Request timing and ML model performance tracking
- **Error Handling**: Graceful error handling with detailed error responses

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Architecture Overview](#-architecture-overview)
- [API Documentation](#-api-documentation)
- [Development Setup](#-development-setup)
- [Production Deployment](#-production-deployment)
- [Configuration](#-configuration)
- [Testing](#-testing)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Docker & Docker Compose
- MySQL 8.0+ (or use Docker)
- Redis 7+ (or use Docker)

### Docker Setup (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/fraudnet-ai.git
   cd fraudnet-ai
   ```

2. **Start the development environment**
   ```bash
   make docker-up
   ```

3. **Initialize the database**
   ```bash
   make migrate
   make seed-data
   ```

4. **Test the API**
   ```bash
   curl -X POST http://localhost:5000/api/v1/transactions \
     -H "Content-Type: application/json" \
     -H "X-API-Key: your-api-key" \
     -d '{
       "user_id": "user_001",
       "amount": 100.00,
       "merchant": "Amazon",
       "merchant_category": "online",
       "payment_method": "credit_card"
     }'
   ```

### Manual Setup

1. **Clone and setup virtual environment**
   ```bash
   git clone https://github.com/your-username/fraudnet-ai.git
   cd fraudnet-ai
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp .env.template .env
   # Edit .env with your configuration
   ```

4. **Setup database and start services**
   ```bash
   # Start MySQL and Redis (or use Docker)
   docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql:8.0
   docker run -d -p 6379:6379 redis:7-alpine
   
   # Initialize database
   python -c "from app.models.database import create_tables; create_tables()"
   
   # Start the application
   flask run
   ```

## 🏗 Architecture Overview

FraudNet.AI follows a modular, microservices-ready architecture:

```
┌─────────────────────────────────────────────────────────────┐
│                     API Gateway (Nginx)                      │
├─────────────────────────────────────────────────────────────┤
│                     Flask Application                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ Transaction │  │   Model     │  │    Health &         │  │
│  │     API     │  │ Management  │  │   Monitoring        │  │
│  │             │  │     API     │  │                     │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                   Security Middleware                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │    Auth     │  │    Rate     │  │    Input            │  │
│  │Management   │  │  Limiting   │  │  Validation         │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                    Core Components                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   Feature   │  │    Model    │  │     Fraud           │  │
│  │ Engineering │  │  Training   │  │   Detection         │  │
│  │             │  │             │  │    Engine           │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                    Data Layer                                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   MySQL     │  │    Redis    │  │    File System      │  │
│  │ (Database)  │  │  (Cache)    │  │   (Artifacts)       │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Core Components

- **Feature Engineering Pipeline**: Ensures training-inference parity with versioned schemas
- **Model Training System**: Automated hyperparameter tuning and model evaluation
- **Real-time Inference Engine**: High-performance fraud detection with model caching
- **Security Layer**: Authentication, authorization, and rate limiting
- **Database Layer**: MySQL for persistent storage, Redis for caching and sessions

## 📚 API Documentation

### Authentication

All API endpoints require authentication via API key:

```bash
curl -H "X-API-Key: your-api-key" http://localhost:5000/api/v1/health
```

### Core Endpoints

#### Transactions

**Create Transaction**
```http
POST /api/v1/transactions
Content-Type: application/json
X-API-Key: your-api-key

{
  "user_id": "user_001",
  "amount": 150.50,
  "merchant": "Amazon",
  "merchant_category": "online",
  "location_country": "US",
  "location_city": "New York",
  "payment_method": "credit_card",
  "device_type": "web"
}
```

**Response:**
```json
{
  "transaction_id": 123,
  "fraud_probability": 0.15,
  "risk_level": "low",
  "prediction_id": 456,
  "processing_time_ms": 89,
  "features_used": ["amount_zscore", "merchant_frequency", "..."],
  "model_version": "v1.2"
}
```

**Get Transaction**
```http
GET /api/v1/transactions/123
X-API-Key: your-api-key
```

**Bulk Transaction Processing**
```http
POST /api/v1/transactions/bulk
Content-Type: application/json
X-API-Key: your-api-key

{
  "transactions": [
    { "user_id": "user_001", "amount": 100.00, ... },
    { "user_id": "user_002", "amount": 250.00, ... }
  ]
}
```

#### Model Management

**Train New Model**
```http
POST /api/v1/models/train
X-API-Key: your-api-key

{
  "algorithm": "xgboost",
  "hyperparameters": {
    "n_estimators": 200,
    "max_depth": 8,
    "learning_rate": 0.1
  }
}
```

**Get Model Metrics**
```http
GET /api/v1/models/v1.2/metrics
X-API-Key: your-api-key
```

#### Health & Monitoring

**Health Check**
```http
GET /api/v1/health
```

**Detailed Health**
```http
GET /api/v1/health/detailed
X-API-Key: your-api-key
```

### Error Responses

All endpoints return consistent error responses:

```json
{
  "error": "Validation failed",
  "message": "Amount cannot be negative",
  "timestamp": "2024-01-15T10:30:00Z",
  "correlation_id": "abc-123-def"
}
```

### Rate Limiting

API endpoints are rate-limited per user:

- **Transaction Creation**: 50 requests/minute
- **Transaction Reads**: 100 requests/minute  
- **Bulk Processing**: 10 requests/minute
- **Model Training**: 5 requests/hour

Rate limit headers are included in responses:

```
X-RateLimit-Limit: 50
X-RateLimit-Remaining: 47
X-RateLimit-Reset: 1642248600
```

## 💻 Development Setup

### Environment Setup

1. **Clone and setup**
   ```bash
   git clone https://github.com/your-username/fraudnet-ai.git
   cd fraudnet-ai
   make install
   ```

2. **Environment configuration**
   ```bash
   cp .env.template .env
   # Edit .env file with your settings
   ```

3. **Start development environment**
   ```bash
   make docker-up
   ```

### Development Workflow

**Run tests**
```bash
make test              # Run all tests
make test-unit         # Unit tests only
make test-integration  # Integration tests only
make test-cov          # With coverage report
```

**Code quality**
```bash
make lint              # Run linting
make format            # Format code
make type-check        # Type checking
```

**Database operations**
```bash
make reset-db          # Reset database
make migrate           # Run migrations
make seed-data         # Seed with sample data
```

**Model training**
```bash
make train-model       # Train new model
```

### Development Tools

- **Hot reloading**: Flask development server with auto-reload
- **Database debugging**: SQL query logging in development mode
- **API testing**: Postman collection and curl examples
- **Code formatting**: Black, isort, flake8
- **Type checking**: MyPy with strict configuration

## 🚀 Production Deployment

### Docker Deployment (Recommended)

1. **Build production image**
   ```bash
   make prod-build
   ```

2. **Deploy with docker-compose**
   ```bash
   # Copy production environment file
   cp .env.production .env
   
   # Edit .env with production values
   vim .env
   
   # Start production stack
   make prod-up
   ```

### Manual Deployment

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set production environment**
   ```bash
   export FLASK_ENV=production
   export SECRET_KEY="your-secure-secret-key"
   export DATABASE_URL="mysql+pymysql://user:pass@host/db"
   ```

3. **Initialize database**
   ```bash
   python -c "from app.models.database import create_tables; create_tables()"
   ```

4. **Start with Gunicorn**
   ```bash
   gunicorn --bind 0.0.0.0:5000 --workers 4 run:app
   ```

### Nginx Configuration

```nginx
upstream fraudnet_app {
    server app:5000;
}

server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://fraudnet_app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

### Environment Variables (Production)

```bash
# Security (REQUIRED)
SECRET_KEY=your-256-bit-secret-key
JWT_SECRET_KEY=your-jwt-secret-key

# Database
DATABASE_URL=mysql+pymysql://user:password@host:3306/fraudnet
DATABASE_POOL_SIZE=20

# Redis
REDIS_URL=redis://redis:6379/0

# Monitoring
PROMETHEUS_ENABLED=true
LOG_LEVEL=WARNING
```

### Health Monitoring

The system provides comprehensive health checks:

- **Liveness probe**: `/api/v1/health/live`
- **Readiness probe**: `/api/v1/health/ready`
- **Detailed health**: `/api/v1/health/detailed`

Kubernetes deployment example:

```yaml
livenessProbe:
  httpGet:
    path: /api/v1/health/live
    port: 5000
  initialDelaySeconds: 30
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /api/v1/health/ready
    port: 5000
  initialDelaySeconds: 5
  periodSeconds: 5
```

## ⚙️ Configuration

### Environment Files

- **Development**: `.env` or environment variables
- **Production**: `.env.production` or container environment
- **Testing**: Configured in test files

### Key Configuration Options

| Variable | Default | Description |
|----------|---------|-------------|
| `FLASK_ENV` | `development` | Application environment |
| `SECRET_KEY` | Required | Flask secret key |
| `DATABASE_URL` | Required | Database connection string |
| `REDIS_URL` | `redis://localhost:6379/0` | Redis connection string |
| `RATE_LIMIT_ENABLED` | `true` | Enable rate limiting |
| `RATE_LIMIT_PER_MINUTE` | `100` | Requests per minute limit |
| `MODEL_CACHE_TTL` | `3600` | Model cache TTL in seconds |
| `LOG_LEVEL` | `INFO` | Logging level |

### Model Configuration

```python
# Model training parameters
MODEL_RETRAIN_THRESHOLD = 0.05  # Retrain if accuracy drops by 5%
MODEL_CACHE_TTL = 3600          # Cache models for 1 hour
FEATURE_WINDOW_HOURS = 24       # Feature extraction window
```

### Security Configuration

```python
# Authentication
API_KEY_HEADER = "X-API-Key"
JWT_ACCESS_TOKEN_EXPIRES = 3600

# Rate limiting
RATE_LIMIT_PER_MINUTE = 100
RATE_LIMIT_BURST = 20

# CORS (production should be specific domains)
CORS_ORIGINS = "https://your-frontend-domain.com"
```

## 🧪 Testing

### Test Structure

```
tests/
├── unit/                 # Unit tests
│   ├── test_models.py
│   ├── test_features.py
│   └── test_ml.py
├── integration/          # Integration tests
│   ├── test_api.py
│   ├── test_database.py
│   └── test_security.py
├── fixtures/             # Test fixtures
│   └── sample_data.py
└── conftest.py          # Test configuration
```

### Running Tests

```bash
# All tests
make test

# Specific test categories
make test-unit
make test-integration

# With coverage
make test-cov

# Specific test file
pytest tests/unit/test_models.py -v

# Specific test
pytest tests/unit/test_models.py::TestUser::test_create_user -v
```

### Test Coverage

The test suite maintains >80% code coverage across:

- **Model operations**: User, Transaction, Prediction models
- **API endpoints**: All REST endpoints with various scenarios  
- **Feature engineering**: Training-inference parity validation
- **Security**: Authentication, rate limiting, validation
- **ML components**: Model training, evaluation, inference

### Performance Testing

```bash
# Load testing with Apache Bench
ab -n 1000 -c 10 -H "X-API-Key: your-key" \
   http://localhost:5000/api/v1/health

# Database performance testing
python tests/performance/test_db_performance.py
```

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Development Process

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes**
   - Follow PEP 8 style guidelines
   - Add tests for new functionality
   - Update documentation as needed

4. **Run the test suite**
   ```bash
   make test
   make lint
   make type-check
   ```

5. **Submit a pull request**

### Code Standards

- **Python**: PEP 8 compliance, type hints required
- **Docstrings**: Google-style docstrings for all public methods
- **Testing**: Test coverage >80% for new code
- **Security**: Security review required for authentication/authorization changes

### Commit Messages

Use conventional commit format:

```
feat: add new fraud detection algorithm
fix: resolve database connection pooling issue
docs: update API documentation
test: add integration tests for bulk processing
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

### Documentation

- **API Reference**: [docs/api.md](docs/api.md)
- **Deployment Guide**: [docs/deployment.md](docs/deployment.md)
- **Architecture Guide**: [docs/architecture.md](docs/architecture.md)

### Getting Help

- **Issues**: [GitHub Issues](https://github.com/your-username/fraudnet-ai/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/fraudnet-ai/discussions)
- **Security**: Email security@yourcompany.com for security issues

### Monitoring & Alerts

- **Application logs**: Structured JSON logs with correlation IDs
- **Metrics**: Prometheus metrics available at `:8000/metrics`
- **Health checks**: Multiple health check endpoints for monitoring
- **Error tracking**: Detailed error responses with correlation IDs

---

**FraudNet.AI** - Built with ❤️ for enterprise fraud detection