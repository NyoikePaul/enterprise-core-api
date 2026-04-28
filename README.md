# Enterprise Core API
![CI/CD](https://github.com/Daniel815266/enterprise-core-api/actions/workflows/main.yml/badge.svg)

Production-grade FastAPI backend architecture.
=======
![Build Status](https://github.com/Daniel815266/enterprise-core-api/actions/workflows/main.yml/badge.svg)
#  Enterprise Core API & Infrastructure


##  Tech Stack
- **Framework:** FastAPI (Python 3.11+)
- **ORM:** SQLAlchemy + Alembic
- **Infra:** Terraform + Docker
- **Security:** JWT + OAuth2 + Bandit Scanning


## 🚀 Setup

docker-compose up --build

##  System Architecture
* **Backend:** FastAPI (Async Python 3.11+)
* **Database:** PostgreSQL with SQLAlchemy ORM
* **Infrastructure:** Terraform (IaC) for automated provisioning
* **Deployment:** Docker & GitHub Actions (CI/CD)


## Architecture: Clean DDD
This API follows Clean Architecture principles:
- **Domain**: Core entities and repository interfaces.
- **Application**: Use cases and business logic orchestration.
- **Infrastructure**: Concrete implementations (PostgreSQL, M-Pesa, E-TIMS).
- **API**: FastAPI routers and versioned entry points.## Architecture: Clean DDD
##  Cloud Automation Features
* **Zero-Touch Provisioning:** The `infra/` directory contains Terraform configurations to spin up a production-ready Linux environment in minutes.
* **Automated Security:** Includes pre-configured GitHub Actions to run security audits and unit tests on every push.
* **Containerization:** Optimized Multi-stage Docker builds to keep image sizes small and secure.

##  Getting Started
1. **Local Dev:** `docker-compose up --build`
2. **Infrastructure:** `cd infra/terraform && terraform apply`
3. **Docs:** Access Swagger UI at `/docs` once the server is running.


*Professional-grade engineering for long-term scalability.*
**
<img width="1358" height="728" alt="image" src="https://github.com/user-attachments/assets/0c06be13-dfdd-4a9c-aa4b-8802014ea0c4" />


