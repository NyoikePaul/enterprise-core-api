![Build Status](https://github.com/Daniel815266/enterprise-core-api/actions/workflows/main.yml/badge.svg)

![Build Status](https://github.com/Daniel815266/enterprise-core-api/actions/workflows/main.yml/badge.svg)
#  Enterprise Core API & Infrastructure

This repository demonstrates a production-grade backend architecture coupled with automated cloud infrastructure. It is designed for scalability, security, and developer productivity.

##  System Architecture
* **Backend:** FastAPI (Async Python 3.11+)
* **Database:** PostgreSQL with SQLAlchemy ORM
* **Infrastructure:** Terraform (IaC) for automated provisioning
* **Deployment:** Docker & GitHub Actions (CI/CD)

##  Cloud Automation Features
* **Zero-Touch Provisioning:** The `infra/` directory contains Terraform configurations to spin up a production-ready Linux environment in minutes.
* **Automated Security:** Includes pre-configured GitHub Actions to run security audits and unit tests on every push.
* **Containerization:** Optimized Multi-stage Docker builds to keep image sizes small and secure.

##  Getting Started
1. **Local Dev:** `docker-compose up --build`
2. **Infrastructure:** `cd infra/terraform && terraform apply`
3. **Docs:** Access Swagger UI at `/docs` once the server is running.

---
*Professional-grade engineering for long-term scalability.*
