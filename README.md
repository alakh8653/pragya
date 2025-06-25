# Pragya

This repository includes an example implementation of a modern online learning platform.
The code lives under `online_learning_platform/` and consists of a FastAPI backend,
a small React frontend, deployment scripts, and documentation. The backend exposes
basic API endpoints for authentication, user management, courses, and more using
in-memory data structures. The backend exposes a `create_app()` function that
constructs the FastAPI application with all routers attached. Additional modules
cover assignments, assessments, analytics, messaging, notifications and
payments. The project includes Docker and Kubernetes manifests as well as a
minimal Terraform configuration.
