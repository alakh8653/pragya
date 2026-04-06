# Online Learning Platform

This directory contains an example implementation for an online learning platform.
It demonstrates a basic FastAPI backend, a minimal React frontend, and
infrastructure configuration using Docker, Kubernetes, and Terraform. The backend
stores data in memory for demonstration and exposes endpoints for users,
authentication, courses, assignments, assessments, analytics and more. Update
and delete operations are implemented for most resources, demonstrating common
CRUD patterns.

The backend application is assembled via `backend.main.create_app` which returns
a fully configured FastAPI instance ready to run with Uvicorn or in tests.

- **backend/** – API source code and tests
- **frontend/** – React application
- **infrastructure/** – deployment artifacts
- **data/** – database migrations and seed data
- **docs/** – project documentation
- **scripts/** – helper scripts for development
