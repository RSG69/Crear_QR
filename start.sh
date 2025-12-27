#!/bin/bash
set -e

# Instalar dependencias del sistema necesarias para Reflex
apt-get update
apt-get install -y unzip

# Puerto Railway
export PORT=${PORT:-3000}

# Build frontend
reflex export --env prod

# Run server
reflex run \
  --env prod \
  --backend-host 0.0.0.0 \
  --backend-port $PORT \
  --single-port

