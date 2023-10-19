#!/bin/bash

echo "Building..."

docker build -f ./frontend/Dockerfile -t flask_docker_app_frontend ./frontend
docker build -f ./backend_y/Dockerfile -t flask_docker_app_backend_y ./backend_y
docker build -f ./backend_z/Dockerfile -t flask_docker_app_backend_z ./backend_z