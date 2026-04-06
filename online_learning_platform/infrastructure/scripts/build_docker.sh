#!/usr/bin/env bash
set -e

docker build -t olp-backend -f ../docker/Dockerfile.backend ../..
docker build -t olp-frontend -f ../docker/Dockerfile.frontend ../..
