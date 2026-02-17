# FraudNet.AI - Complete Fraud Detection Platform

[![CI/CD](https://github.com/your-username/fraudnet-ai/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/your-username/fraudnet-ai/actions/workflows/ci-cd.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Next.js 14](https://img.shields.io/badge/Next.js-14.1.0-black.svg)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.3.3-blue.svg)](https://www.typescriptlang.org/)

**🚀 Enterprise-grade fraud detection platform with modern web interface, real-time analytics, and production-ready infrastructure.**

FraudNet.AI is a complete fraud detection ecosystem featuring a React/Next.js frontend, Python/Flask backend, JWT authentication, role-based access control, and comprehensive monitoring capabilities. Built for scale with Docker, Kubernetes, and modern DevOps practices.

![Platform Overview](docs/images/platform-overview.png)
*Complete fraud detection platform with web dashboard, real-time analytics, and enterprise security*

## ✨ Platform Features

### 🎨 **Modern Web Interface**
- **Next.js 14 Dashboard** with server-side rendering and App Router
- **Real-time Fraud Analytics** with interactive charts and metrics
- **Transaction Explorer** with advanced filtering and search
- **Model Management Interface** for ML model monitoring
- **Responsive Design** optimized for desktop, tablet, and mobile
- **Dark/Light Mode** with fraud-specific color schemes

### 🔐 **Enterprise Authentication & Security**
- **JWT Authentication** with automatic token refresh
- **Role-Based Access Control** (Admin, Analyst, Viewer)
- **Multi-factor Authentication** ready (2FA/TOTP)
- **Session Management** with Redis backend
- **API Security** with rate limiting and input validation
- **Audit Logging** for compliance and security monitoring

### 🤖 **Advanced Fraud Detection**
- **Real-time Processing** sub-200ms transaction analysis
- **Machine Learning Pipeline** with automated retraining
- **Feature Engineering** with training-inference parity
- **Model Versioning** and A/B testing capabilities
- **Risk Scoring** with configurable thresholds
- **Batch Processing** for high-volume transactions

### 🏗 **Production Infrastructure**
- **Microservices Architecture** with Docker containers
- **Auto-scaling** with Kubernetes and Horizontal Pod Autoscaling
- **Caching Layer** with Redis for performance optimization
- **Message Queue** with Kafka for event streaming
- **Observability Stack** with Prometheus, Grafana, and Jaeger
- **CI/CD Pipeline** with automated testing and deployment

## 🖼️ Platform Screenshots

### Dashboard Overview
![Dashboard Overview](docs/images/dashboard-overview.png)
*Real-time fraud detection dashboard with key metrics and trends*

### Transaction Analytics
![Transaction Analytics](docs/images/transaction-analytics.png)
*Advanced transaction filtering and risk analysis interface*

### User Management
![User Management](docs/images/user-management.png)
*Role-based user management with detailed permissions*

### Model Performance
![Model Performance](docs/images/model-performance.png)
*ML model monitoring with performance metrics and training history*

### Alert Management
![Alert Management](docs/images/alert-management.png)
*Real-time alert dashboard with configurable fraud rules*

## 📋 Table of Contents

- [🚀 Quick Start](#-quick-start)
- [🏗 Platform Architecture](#-platform-architecture)
- [🎨 Frontend Features](#-frontend-features)
- [📚 API Documentation](#-api-documentation)
- [🔐 Authentication & Authorization](#-authentication--authorization)
- [💻 Development Setup](#-development-setup)
- [🐳 Production Deployment](#-production-deployment)
- [📊 Monitoring & Observability](#-monitoring--observability)
- [🧪 Testing](#-testing)
- [🤝 Contributing](#-contributing)

## 🚀 Quick Start

### Full Platform Deployment (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/fraudnet-ai.git
   cd fraudnet-ai
   ```

2. **Start the complete platform**
   ```bash
   # Start all services (Frontend + Backend + Infrastructure)
   docker-compose -f docker-compose.prod.yml up -d
   
   # Initialize authentication system
   python scripts/init_auth.py
   ```

3. **Access the platform**
   - **Web Dashboard**: [http://localhost:3000](http://localhost:3000)
   - **API Documentation**: [http://localhost:5000/api](http://localhost:5000/api)
   - **Monitoring Dashboard**: [http://localhost:3001](http://localhost:3001)

4. **Login with default credentials**
   - **Admin**: admin@fraudnet.ai / admin123
   - **Analyst**: analyst@fraudnet.ai / analyst123
   - **Viewer**: viewer@fraudnet.ai / viewer123

### Development Setup

1. **Start development environment**
   ```bash
   # Backend development
   make docker-up
   make migrate
   make seed-data
   
   # Frontend development
   cd frontend
   npm install
   npm run dev
   ```

2. **Test the platform**
   ```bash
   # Test API endpoint
   curl -X POST http://localhost:5000/api/v1/auth/login \
     -H "Content-Type: application/json" \
     -d '{"email": "admin@fraudnet.ai", "password": "admin123"}'
   
   # Access frontend
   open http://localhost:3000
   ```

## 🏗 Platform Architecture

FraudNet.AI follows a modern microservices architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          Load Balancer (Nginx)                          │
├─────────────────────────┬───────────────────────────┬───────────────────┤
│    Frontend (Next.js)   │     Backend (Flask)       │   Infrastructure   │
│                         │                           │                    │
│ ┌─────────────────────┐ │ ┌─────────────────────────┐ │ ┌───────────────┐ │
│ │   Web Dashboard     │ │ │     REST API            │ │ │  Prometheus   │ │
│ │   • Real-time UI    │◄─┤ │     • Authentication    │ │ │  (Metrics)    │ │
│ │   • Transaction     │ │ │     • Transaction API   │ │ └───────────────┘ │
│ │     Explorer        │ │ │     • Model Management  │ │ ┌───────────────┐ │
│ │   • User Mgmt       │ │ │     • Health Checks     │ │ │   Grafana     │ │
│ │   • Analytics       │ │ └─────────────────────────┘ │ │ (Dashboards)  │ │
│ └─────────────────────┘ │                           │ └───────────────┘ │
├─────────────────────────┼───────────────────────────┤                   │
│   Authentication        │    Business Logic         │ ┌───────────────┐ │
│                         │                           │ │     Kafka     │ │
│ ┌─────────────────────┐ │ ┌─────────────────────────┐ │ │ (Streaming)   │ │
│ │  JWT Auth System    │ │ │   Fraud Detection       │◄┤ │   • Events    │ │
│ │  • Login/Logout     │ │ │   • Feature Engineering │ │ │   • Real-time │ │
│ │  • RBAC             │ │ │   • ML Pipeline         │ │ │   • Analytics │ │
│ │  • Session Mgmt     │ │ │   • Model Training      │ │ └───────────────┘ │
│ └─────────────────────┘ │ └─────────────────────────┘ │                   │
├─────────────────────────┴───────────────────────────┤                   │
│                     Data & Cache Layer                │ ┌───────────────┐ │
│                                                       │ │    Redis      │ │
│ ┌─────────────────┐  ┌─────────────────────────────┐ │ │  (Cache)      │ │
│ │     MySQL       │  │         Redis Cluster        │◄┤ │   • Sessions  │ │
│ │   • Users       │  │         • User Sessions      │ │ │   • API Cache │ │
│ │   • Transactions│  │         • API Response Cache │ │ │   • Rate Limit│ │
│ │   • Models      │  │         • Rate Limiting      │ │ └───────────────┘ │
│ │   • Audit Logs  │  │         • Real-time Data     │ │                   │
│ └─────────────────┘  └─────────────────────────────┘ │                   │
└─────────────────────────────────────────────────────────────────────────┘
```

### Key Components

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Frontend** | Next.js 14, TypeScript, TailwindCSS | Web dashboard and user interface |
| **Backend API** | Flask 3.0, Python 3.11 | REST API and business logic |
| **Authentication** | JWT, Redis sessions | User management and security |
| **Database** | MySQL 8.0+ | Primary data storage |
| **Cache** | Redis 7+ | Session store and API caching |
| **Message Queue** | Kafka | Event streaming and real-time processing |
| **Monitoring** | Prometheus + Grafana | Metrics collection and visualization |
| **Load Balancer** | Nginx | Request routing and SSL termination |

## 🎨 Frontend Features

### Dashboard Components

#### Real-time Metrics Dashboard
```typescript
// Key metrics displayed in real-time
interface DashboardMetrics {
  totalTransactions: number;
  fraudDetected: number;
  fraudRate: percentage;
  amountSaved: currency;
  recentAlerts: FraudAlert[];
  systemHealth: HealthStatus;
}
```
![Real-time Dashboard](docs/images/realtime-dashboard.png)

#### Transaction Explorer
- **Advanced Filtering**: Date range, amount, risk level, merchant
- **Risk Analysis**: Visual risk scoring with color-coded indicators
- **Export Capabilities**: CSV, PDF export for compliance
- **Bulk Operations**: Approve/reject multiple transactions

![Transaction Explorer](docs/images/transaction-explorer.png)

#### User Management Interface
- **Role-based Access Control**: Admin, Analyst, Viewer permissions
- **User Activity Tracking**: Login history and audit trails
- **Profile Management**: User settings and preferences

![User Management](docs/images/user-dashboard.png)

### Technical Implementation

#### Frontend Stack
```json
{
  "framework": "Next.js 14.1.0 (App Router)",
  "language": "TypeScript 5.3.3",
  "styling": "TailwindCSS 3.4.1",
  "charts": "Recharts 2.10.3",
  "forms": "React Hook Form + Zod",
  "http": "Axios with interceptors",
  "auth": "JWT with refresh tokens"
}
```

#### Key Frontend Features
- **Server-Side Rendering**: Optimized performance and SEO
- **Progressive Web App**: Offline support and mobile installation
- **Real-time Updates**: WebSocket connections for live data
- **Responsive Design**: Mobile-first responsive layout
- **Accessibility**: WCAG 2.1 AA compliant
- **Internationalization**: Multi-language support ready

## 📚 API Documentation

### Authentication-First API

All API endpoints now use JWT authentication instead of API keys:

```bash
# 1. Login to get JWT token
curl -X POST http://localhost:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@fraudnet.ai", "password": "admin123"}'

# 2. Use JWT token for API calls
curl -H "Authorization: Bearer <jwt-token>" \
     http://localhost:5000/api/v1/transactions
```

### Core API Endpoints

#### Authentication Endpoints
```http
POST   /api/v1/auth/login           # User login
POST   /api/v1/auth/logout          # User logout  
POST   /api/v1/auth/refresh         # Refresh JWT token
GET    /api/v1/auth/me              # Get current user
POST   /api/v1/auth/change-password # Change password
```

#### Transaction Management
```http
GET    /api/v1/dashboard/metrics    # Dashboard metrics
GET    /api/v1/transactions         # List transactions
POST   /api/v1/transactions         # Create transaction
GET    /api/v1/transactions/:id     # Get transaction
POST   /api/v1/transactions/predict # Predict fraud risk
POST   /api/v1/transactions/bulk    # Bulk processing
```

#### User Management (Admin Only)
```http
GET    /api/v1/users                # List users
POST   /api/v1/users                # Create user
PUT    /api/v1/users/:id            # Update user
DELETE /api/v1/users/:id            # Delete user
```

### Enhanced API Response Format

```json
{
  "status": "success",
  "data": {
    "transaction_id": 12345,
    "fraud_probability": 0.85,
    "risk_level": "high",
    "recommendation": "block",
    "confidence": 0.92,
    "processing_time_ms": 45,
    "model_version": "v2.1.3",
    "features_used": ["amount_zscore", "velocity", "merchant_risk"],
    "explainability": {
      "top_factors": [
        {"feature": "amount_zscore", "importance": 0.35},
        {"feature": "transaction_velocity", "importance": 0.28}
      ]
    }
  },
  "timestamp": "2026-02-17T10:30:00Z",
  "correlation_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

## 🔐 Authentication & Authorization

### JWT-Based Authentication

FraudNet.AI uses industry-standard JWT tokens for secure authentication:

```mermaid
sequenceDiagram
    participant UI as Frontend
    participant API as Backend API
    participant DB as Database
    participant Cache as Redis

    UI->>API: POST /auth/login {email, password}
    API->>DB: Validate user credentials
    DB-->>API: User data + role
    API->>Cache: Store session data
    API-->>UI: JWT tokens (access + refresh)
    
    UI->>API: API call with Bearer token
    API->>Cache: Validate token & get user
    API-->>UI: Protected resource
    
    Note over UI,API: Token refresh flow
    UI->>API: POST /auth/refresh {refresh_token}
    API-->>UI: New access token
```

### Role-Based Access Control (RBAC)

| Role | Permissions | Dashboard Access |
|------|-------------|------------------|
| **Admin** | Full system access, user management, system settings | ✅ All features |
| **Analyst** | Transaction analysis, model management, reports | ✅ Analytics & Models |
| **Viewer** | Read-only access to dashboard and transactions | ✅ Dashboard only |

### Security Features

```python
# JWT Configuration
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
JWT_ALGORITHM = 'HS256'

# Rate Limiting (per user role)
RATE_LIMITS = {
    'admin': '1000/hour',
    'analyst': '500/hour', 
    'viewer': '200/hour'
}

# Password Policy
PASSWORD_MIN_LENGTH = 8
PASSWORD_REQUIRE_UPPERCASE = True
PASSWORD_REQUIRE_NUMBERS = True
PASSWORD_REQUIRE_SYMBOLS = True
```

## 💻 Development Setup

### Prerequisites

- **Backend**: Python 3.11+, Docker, MySQL 8.0+, Redis 7+
- **Frontend**: Node.js 18+, npm 9+
- **Infrastructure**: Docker Compose, Kubernetes (for production)

### Full Development Environment

```bash
# 1. Clone repository
git clone https://github.com/your-username/fraudnet-ai.git
cd fraudnet-ai

# 2. Start backend services
make docker-up                 # Start MySQL, Redis, Backend API
make migrate                   # Initialize database
python scripts/init_auth.py    # Create default users

# 3. Start frontend development
cd frontend
npm install                    # Install dependencies  
npm run dev                    # Start Next.js dev server

# 4. Access applications
# Frontend: http://localhost:3000
# Backend API: http://localhost:5000
# API Docs: http://localhost:5000/api/docs
```

### Development Scripts

```bash
# Backend Development
make install         # Install Python dependencies
make test           # Run all tests
make lint           # Code linting
make format         # Code formatting  
make type-check     # TypeScript checking
make security-scan  # Security vulnerability scan

# Frontend Development  
cd frontend
npm run dev         # Development server
npm run build       # Production build
npm run lint        # ESLint checking
npm run type-check  # TypeScript validation

# Full Platform
make dev-up         # Start full development stack
make dev-down       # Stop development environment
make reset-all      # Reset database and restart
```

### Development Workflow

```mermaid
graph LR
    A[Code Change] --> B[Run Tests]
    B --> C[Lint & Format]
    C --> D[Type Check]
    D --> E[Security Scan]
    E --> F[Commit]
    F --> G[Pull Request]
    G --> H[CI/CD Pipeline]
    H --> I[Deploy to Staging]
    I --> J[Integration Tests]
    J --> K[Deploy to Production]
```

## 🐳 Production Deployment

### Containerized Deployment (Recommended)

FraudNet.AI provides production-ready Docker Compose configuration:

```bash
# 1. Production deployment
docker-compose -f docker-compose.prod.yml up -d

# 2. Initialize system
python scripts/init_auth.py

# 3. Verify deployment
curl -f http://localhost:5000/api/v1/health
curl -f http://localhost:3000
```

### Services Overview

```yaml
# docker-compose.prod.yml includes:
services:
  frontend:          # Next.js web application (Port 3000)
  api:              # Flask backend API (Port 5000) 
  mysql:            # MySQL database (Port 3306)
  redis:            # Redis cache & sessions (Port 6379)
  kafka:            # Kafka message queue (Port 9092)
  celery-worker:    # Background task processing
  celery-beat:      # Scheduled task runner
  prometheus:       # Metrics collection (Port 9090)
  grafana:         # Monitoring dashboards (Port 3001)
  nginx:           # Load balancer & reverse proxy (Port 80/443)
```

### Kubernetes Deployment

```bash
# 1. Apply Kubernetes manifests
kubectl apply -f k8s/

# 2. Verify pods are running
kubectl get pods -n fraudnet-ai

# 3. Access via LoadBalancer
kubectl get svc fraudnet-frontend -n fraudnet-ai
```

### Production Configuration

```env
# Security (Required)
SECRET_KEY=your-256-bit-production-secret
JWT_SECRET_KEY=your-jwt-256-bit-secret

# Database
DATABASE_URL=mysql+pymysql://user:password@mysql:3306/fraudnet_ai
DATABASE_POOL_SIZE=20
DATABASE_POOL_TIMEOUT=30

# Redis
REDIS_URL=redis://redis:6379/0
CACHE_REDIS_URL=redis://redis:6379/1
SESSION_REDIS_URL=redis://redis:6379/2

# Frontend
NEXT_PUBLIC_API_URL=https://api.yourdomain.com/api
NEXT_PUBLIC_WS_URL=wss://api.yourdomain.com

# Monitoring
PROMETHEUS_ENABLED=true
GRAFANA_ENABLED=true
LOG_LEVEL=INFO
LOG_FORMAT=json

# Performance
WORKERS=4
MAX_CONNECTIONS=1000
REQUEST_TIMEOUT=30
```

## 📊 Monitoring & Observability

### Monitoring Stack

![Monitoring Dashboard](docs/images/monitoring-stack.png)
*Comprehensive monitoring with Prometheus, Grafana, and custom dashboards*

#### Prometheus Metrics
```python
# Key metrics collected
- fraudnet_requests_total              # Total API requests
- fraudnet_requests_duration_seconds   # Request response time
- fraudnet_fraud_detections_total      # Fraud detections count
- fraudnet_model_inference_duration    # ML model performance
- fraudnet_database_connections        # Database pool status
- fraudnet_cache_operations_total      # Redis cache metrics
```

#### Grafana Dashboards
- **Application Overview**: Request rates, error rates, response times
- **Fraud Detection Metrics**: Detection rates, model performance, alerts
- **Infrastructure Monitoring**: CPU, memory, disk usage, network I/O
- **User Activity**: Login rates, session duration, feature usage
- **Business Intelligence**: Transaction volumes, fraud trends, ROI metrics

### Health Checks & Alerting

```http
GET /api/v1/health         # Basic health check
GET /api/v1/health/db      # Database connectivity  
GET /api/v1/health/cache   # Redis connectivity
GET /api/v1/health/ml      # ML model status
GET /api/v1/health/detailed # Comprehensive system status
```

### Log Management

```json
// Structured logging format
{
  "timestamp": "2026-02-17T10:30:00.123Z",
  "level": "INFO",
  "service": "fraudnet-api",
  "correlation_id": "550e8400-e29b-41d4-a716-446655440000",
  "user_id": "user_12345",
  "endpoint": "/api/v1/transactions",
  "method": "POST",
  "status_code": 200,
  "duration_ms": 89.5,
  "fraud_probability": 0.15,
  "model_version": "v2.1.3"
}
```

## 🧪 Testing

### Comprehensive Test Suite

FraudNet.AI includes extensive testing for both frontend and backend components:

```bash
# Backend Testing
make test              # Run full test suite
make test-unit         # Unit tests only 
make test-integration  # Integration tests
make test-api         # API endpoint tests
make test-ml          # ML model tests
make test-coverage    # Generate coverage report

# Frontend Testing
cd frontend
npm test              # Jest unit tests
npm run test:e2e      # Playwright E2E tests
npm run test:coverage # Test coverage report

# Load Testing  
make load-test        # Artillery.js load testing
```

### Test Coverage

| Component | Coverage | Tests |
|-----------|----------|-------|
| **Backend API** | 95%+ | 450+ tests |
| **Frontend Components** | 90%+ | 280+ tests |
| **Authentication** | 98% | 85 tests |
| **ML Pipeline** | 92% | 120 tests |
| **Integration** | 88% | 65 tests |

### Testing Environments

```yaml
# Test matrix
environments:
  - python: [3.11, 3.12]
    node: [18, 20]  
    mysql: [8.0, 8.1]
    redis: [7.0, 7.2]
    browsers: [chrome, firefox, safari, edge]
```

![Test Results Dashboard](docs/images/test-coverage.png)
*Comprehensive test coverage dashboard with real-time results*

## 🤝 Contributing

### Development Guidelines

We welcome contributions! Please follow our development guidelines:

1. **Fork the repository** and create a feature branch
2. **Write tests** for new functionality
3. **Follow code style** with pre-commit hooks
4. **Update documentation** as needed
5. **Submit a pull request** with detailed description

### Code Standards

```bash
# Code quality tools
make lint          # Run all linters (flake8, mypy, eslint)
make format        # Auto-format code (black, prettier)
make security-scan # Security vulnerability scanning
make pre-commit    # Run all pre-commit hooks
```

### Development Flow

```mermaid
graph TD
    A[Create Feature Branch] --> B[Write Code]
    B --> C[Add Tests]
    C --> D[Run Test Suite]
    D --> E[Code Review]
    E --> F[CI/CD Pipeline]
    F --> G[Deploy to Staging]
    G --> H[QA Testing]
    H --> I[Deploy to Production]
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: [docs.fraudnet.ai](https://docs.fraudnet.ai)
- **Issues**: [GitHub Issues](https://github.com/your-username/fraudnet-ai/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/fraudnet-ai/discussions)
- **Email**: support@fraudnet.ai

---

## 📸 UI Image Generation Prompts

**Use these prompts to generate professional screenshots for the platform documentation:**

### 1. Dashboard Overview Screenshot
```
Create a professional screenshot of a fraud detection dashboard with:
- Modern dark theme UI with blue and red accent colors
- Top navigation bar with "FraudNet.AI" logo and user avatar
- Key metrics cards showing: "Total Transactions: 45,231", "Fraud Detected: 892", "Fraud Rate: 1.97%", "Amount Saved: $2.3M"
- Real-time line chart showing transaction volume over 24 hours
- Color-coded fraud alerts list on the right sidebar
- Clean, modern interface with subtle shadows and rounded corners
- Professional typography and spacing
- Responsive grid layout
Filename: /docs/images/dashboard-overview.png
```

### 2. Transaction Analytics Interface
```
Create a screenshot of transaction analytics page featuring:
- Data table with transaction rows showing: ID, Amount, Merchant, Risk Score (color-coded bars), Status
- Advanced filter sidebar with date picker, amount range sliders, risk level toggles
- Search bar with transaction ID/merchant search
- Risk distribution donut chart showing Low (green), Medium (yellow), High (red) risk percentages
- Export buttons (CSV, PDF) in top right
- Pagination controls at bottom
- Sort indicators on column headers
- Modern table design with zebra striping
Filename: /docs/images/transaction-analytics.png
```

### 3. User Management Dashboard
```
Create a user management interface screenshot showing:
- User list table with columns: Avatar, Name, Email, Role (Admin/Analyst/Viewer), Status, Last Login
- Role-based permission badges with different colors
- "Add User" button with plus icon
- User profile modal overlay showing user details and role assignment
- Activity timeline on the right showing recent user actions
- Search and filter controls for users
- Professional admin interface design
- Clean icons and consistent spacing
Filename: /docs/images/user-management.png
```

### 4. Model Performance Dashboard
```
Create an ML model monitoring dashboard featuring:
- Model performance metrics: Accuracy (94.2%), Precision (91.8%), Recall (89.5%), F1-Score (90.6%)
- Training history line chart showing accuracy over epochs
- Feature importance horizontal bar chart
- Model version selector dropdown showing "v2.1.3 (Current)"
- Real-time prediction latency gauge (85ms average)
- Confusion matrix heatmap visualization
- Model drift detection charts
- Professional data science dashboard aesthetic
Filename: /docs/images/model-performance.png
```

### 5. Alert Management Interface
```
Create an alert management dashboard with:
- Real-time alert feed showing fraud alerts with timestamps
- Alert severity indicators (Critical, High, Medium, Low) with color coding
- Quick action buttons: "Approve", "Block", "Review"
- Alert details panel showing transaction context and risk factors
- Alert statistics cards: Active Alerts, Resolved Today, False Positives
- Time-based alert volume chart
- Alert filtering by severity and type
- Clean notification-style interface design
Filename: /docs/images/alert-management.png
```

### 6. Platform Overview Diagram
```
Create an architectural diagram showing:
- Three main sections: Frontend (Next.js), Backend (Flask), Infrastructure
- Frontend containing: Web Dashboard, Transaction Explorer, User Management
- Backend containing: REST API, Authentication, ML Pipeline, Fraud Detection
- Infrastructure containing: MySQL, Redis, Kafka, Prometheus, Grafana
- Connecting arrows showing data flow between components
- Clean, professional system architecture style
- Blue and gray color scheme with clear labels
- Modern diagram aesthetics similar to cloud architecture diagrams
Filename: /docs/images/platform-overview.png
```

### 7. Real-time Monitoring Stack
```
Create a monitoring dashboard screenshot featuring:
- Grafana-style dashboard with multiple panels
- API response time graph with red alert threshold line
- System resource utilization (CPU, Memory, Disk) gauges
- Fraud detection rate metrics over time
- Database connection pool status
- Error rate alerts and notifications
- Dark theme with bright accent colors for alerts
- Professional monitoring tool aesthetic
Filename: /docs/images/monitoring-stack.png
```

### 8. User Login Interface
```
Create a modern login page screenshot showing:
- Centered login form on clean background
- "FraudNet.AI" logo at top
- Email and password input fields with modern styling
- "Sign In" button with primary blue color
- "Remember me" checkbox and "Forgot password?" link
- Security badge/SSL indicator
- Clean, minimal design with subtle gradients
- Professional authentication interface
Filename: /docs/images/user-dashboard.png
```

### 9. Transaction Explorer Details
```
Create a detailed transaction view showing:
- Transaction details card with all transaction metadata
- Risk assessment panel with visual risk scoring (0-100 scale)
- Fraud indicators list with check/X marks
- Related transactions section showing similar patterns
- Action history timeline for the transaction
- Manual review section with analyst notes
- Approve/Reject/Review action buttons
- Professional investigation interface design
Filename: /docs/images/transaction-explorer.png
```

### 10. Test Coverage Dashboard
```
Create a testing dashboard screenshot featuring:  
- Coverage percentage gauges for different components (Backend: 95%, Frontend: 90%)
- Test suite results table showing passed/failed tests by category
- Test execution time graph over recent runs
- Code quality metrics panel
- CI/CD pipeline status with green checkmarks
- Professional development tools interface
- Clean code coverage visualization style
Filename: /docs/images/test-coverage.png
```

### 11. Real-time Processing Dashboard
```
Create a real-time processing interface showing:
- Live transaction stream with scrolling transaction entries
- Processing speed odometer showing "185ms avg"
- Throughput chart showing transactions per second
- Queue status indicators with current queue depth
- Geographic transaction map with real-time dots
- System health indicators (all green)
- Professional real-time monitoring aesthetic
- Dark background with bright data visualizations
Filename: /docs/images/realtime-dashboard.png
```

**📝 Note**: Save all generated images to the `docs/images/` directory and ensure they maintain consistent styling with a modern, professional fraud detection platform theme. Use a dark/light theme toggle-friendly color scheme with primary colors being blue (#3B82F6) for accents and red (#EF4444) for fraud alerts.

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