#!/bin/bash
# set -eo pipefail
echo "Starting FastAPI backend..."
cd backend 
pipenv run uvicorn bracket.app:app --host localhost --port 8400 --workers 1 --reload &
BACKEND_PID=$!

echo "Starting Next.js frontend..."
cd ../frontend
yarn run dev & FRONTEND_PID=$!

# Trap script to handle shutdown of both processes
trap 'kill $BACKEND_PID $FRONTEND_PID' EXIT

# Wait for both processes to finish
wait $BACKEND_PID $FRONTEND_PID