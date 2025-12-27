#!/bin/bash
export PORT=${PORT:-3000}
reflex run --env prod --backend-host 0.0.0.0 --single-port --port $PORT
