# Lyra AI Agent Backend

This is the backend component of the Lyra AI Agent, a privacy-first desktop AI companion built with Python, FastAPI, and Ollama.

## Project Structure

- `api/` - API routes and WebSocket handlers
- `brain/` - LLM integration and reasoning
- `memory/` - Persistence and context management
- `tools/` - System interaction framework

## Setup

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Run the development server:
   ```bash
   poetry run python main.py
   ```

## API Endpoints

- `GET /health` - Health check endpoint
- `POST /api/v1/chat` - Chat completion endpoint
- `WebSocket /api/v1/ws/chat` - Real-time chat WebSocket

## Dependencies

- Python 3.11+
- FastAPI
- Uvicorn
- Ollama Python client