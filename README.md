# Lyra Voice Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Node.js Version](https://img.shields.io/badge/node.js-18+-green.svg)](https://nodejs.org/)

Welcome to Lyra, a privacy-first, open-source AI voice assistant built for Linux desktops, with a special focus on EndeavourOS.

## What is Lyra?

Lyra is an offline AI assistant that runs completely locally on your machine. No data leaves your computer, no cloud services required. I'm building it to have natural conversations with my desktop - things like:
- "Hey Lyra, open my Python project from yesterday"
- "What did I work on last week?"
- "Show me the status of my git repositories"

## Demo
### WEB GUI
![Screenshot 1](https://res.cloudinary.com/dta7ppwxj/image/upload/v1756645285/Screenshot_20250831_195714_xjucyo.webp)
### Electron GUI
![Screenshot 2](https://res.cloudinary.com/dta7ppwxj/image/upload/v1756645285/Screenshot_20250831_195814_tieex1.webp)
![Screenshot 3](https://res.cloudinary.com/dta7ppwxj/image/upload/v1756645285/Screenshot_20250831_195809_ru8mox.webp)

## Current Status

I've just finished the core foundation (Phase 1)! 🎉

### What's Working Now:
- ✅ Text-based chat with the AI (using Gemma 3 4B model)
- ✅ Beautiful cosmic-themed GUI with starfield animations
- ✅ Persistent conversation history
- ✅ Application launching capabilities
- ✅ WebSocket communication between frontend and backend
- ✅ Electron desktop app support

### Technologies Used:
- **Backend**: Python + FastAPI
- **AI Model**: Gemma 3 4B (via Ollama)
- **Frontend**: HTML/CSS/JS with Electron
- **Voice** (coming soon): faster-whisper for STT, Piper for TTS

## Why I'm Building This

I wanted an AI assistant that:
1. Respects my privacy - everything stays on my machine
2. Integrates naturally with my EndeavourOS desktop
3. Remembers our conversations and learns my preferences
4. Helps me be more productive without being creepy

## Project Structure
```
lyra-voice-assistant/
├── backend/          # Python FastAPI server
│   ├── api/          # API routes and WebSocket handlers
│   ├── brain/        # LLM integration and reasoning
│   ├── memory/       # Conversation history and context
│   ├── tools/        # System interaction tools
│   └── main.py       # Server entry point
├── gui/              # Electron frontend
├── models/           # Local AI models
├── lyra.sh           # Control script to start/stop everything
└── ...
```

## How to Run It

### Prerequisites
- [Ollama](https://ollama.com/) with Gemma 3 4B model (`ollama pull gemma3:4b-it-q4_K_M`)
- [Python 3.11+](https://www.python.org/downloads/) with [Poetry](https://python-poetry.org/)
- [Node.js 18+](https://nodejs.org/en/download)

### Setup & Run
1. Install backend dependencies:
   ```bash
   cd backend
   poetry install
   ```

2. Install frontend dependencies:
   ```bash
   cd gui
   npm install
   ```

3. Start everything with the control script:
   ```bash
   cd ..  # back to project root
   ./lyra.sh start
   ```

4. Access the interface:
   - Web version: http://localhost:5252
   - Electron app: `cd gui && npm start`

### Backend API Endpoints
- `GET /health` - Health check
- `POST /api/v1/chat` - Chat completion
- `WebSocket /api/v1/ws/chat` - Real-time chat

## Development Process

I've planned this project in 5 phases over 20 weeks:

- **Phase 1** (Done): Core foundation ✅
  - Backend server with FastAPI
  - Ollama integration with Gemma 3 4B
  - Basic GUI with WebSocket connection
  - JSON-based memory storage

- **Phase 2**: Voice interface and enhanced GUI
  - Speech-to-text with faster-whisper
  - Text-to-speech with Piper
  - Voice visualization animations

- **Phase 3**: Advanced memory system
  - SQLite database with semantic search
  - Embedding-based context retrieval

- **Phase 4**: Tool expansion
  - Application launcher (Kate, Firefox, etc.)
  - File system operations
  - Development environment tools

- **Phase 5**: Polish and deployment
  - Performance optimization
  - AUR package for Arch/EndeavourOS
  - Documentation and tutorials

Detailed planning can be found in [lyra_planning_md.md](lyra_planning_md.md) and task breakdown in [lyra_tasks_md.md](lyra_tasks_md.md).

## Contributing
This is primarily a personal learning project, but contributions are welcome! If you have ideas for improvements or find a bug, please feel free to open an issue or submit a pull request. Check out the [development plan](lyra_planning_md.md) to see where the project is headed.

## License
MIT - do whatever you want with it :)
