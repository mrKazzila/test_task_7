#!/bin/bash

echo "Running uvicorn..."
uvicorn main:app --reload --host 0.0.0.0 --port 8000 --log-config=config/logger_config.yaml
