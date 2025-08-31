# TASKS.md - Lyra AI Agent Development Tasks

**Project:** Lyra AI Agent
**Version:** 2.0
**Last Updated:** August 2025

---

## Task Categories

- 🧠 **Brain** - LLM Integration & Reasoning
- 💾 **Memory** - Persistence & Context Management  
- 🛠️ **Tools** - System Integration & Actions
- 🎨 **GUI** - User Interface & Experience
- 🔧 **Core** - Infrastructure & Architecture
- 🚀 **Deploy** - Packaging & Distribution

---

## Phase 1: Core Foundation (Weeks 1-4)

### 🔧 Backend Architecture
- [x] **TASK-001** Set up Python project structure with Poetry
  - Priority: High | Estimate: 2h
  - Dependencies: None
  - Deliverable: Basic project skeleton with pyproject.toml

- [x] **TASK-002** Implement FastAPI backend server
  - Priority: High | Estimate: 4h  
  - Dependencies: TASK-001
  - Deliverable: REST API with WebSocket support for GUI communication

- [ ] **TASK-003** Create configuration management system
  - Priority: High | Estimate: 3h
  - Dependencies: TASK-001
  - Deliverable: TOML-based config with user preferences, API endpoints

### 🧠 Brain Implementation  
- [x] **TASK-004** Integrate Ollama client for Gemma 3 4B
  - Priority: High | Estimate: 6h
  - Dependencies: TASK-002
  - Deliverable: LLM service class with prompt management

- [ ] **TASK-005** Implement conversation context assembly
  - Priority: High | Estimate: 4h
  - Dependencies: TASK-004
  - Deliverable: Context builder that formats chat history + memory for LLM

- [ ] **TASK-006** Create prompt templates for different agent modes
  - Priority: Medium | Estimate: 3h
  - Dependencies: TASK-004
  - Deliverable: Template system for reasoning, tool selection, conversation

### 💾 Memory System (Basic)
- [x] **TASK-007** Implement JSON-based memory storage
  - Priority: High | Estimate: 5h
  - Dependencies: TASK-002
  - Deliverable: Memory manager with CRUD operations for conversations

- [ ] **TASK-008** Create conversation history management
  - Priority: High | Estimate: 4h
  - Dependencies: TASK-007
  - Deliverable: Chat history storage with timestamps and metadata

- [ ] **TASK-009** Build user preference learning system
  - Priority: Medium | Estimate: 6h
  - Dependencies: TASK-007
  - Deliverable: Preference tracker that learns from user interactions

### 🛠️ Tools Framework
- [x] **TASK-010** Design tool execution framework
  - Priority: High | Estimate: 5h
  - Dependencies: TASK-002
  - Deliverable: Command pattern implementation for safe tool execution

- [ ] **TASK-011** Implement application launcher tool
  - Priority: High | Estimate: 4h
  - Dependencies: TASK-010
  - Deliverable: Launch desktop apps from natural language commands

- [ ] **TASK-012** Create file system interaction tool
  - Priority: Medium | Estimate: 6h
  - Dependencies: TASK-010
  - Deliverable: Safe file operations within user directories

### 🎨 GUI Integration
- [x] **TASK-013** Connect Electron GUI to FastAPI backend
  - Priority: High | Estimate: 4h
  - Dependencies: TASK-002
  - Deliverable: WebSocket communication between GUI and backend

- [ ] **TASK-014** Enhance status display for agent states
  - Priority: Medium | Estimate: 3h
  - Dependencies: TASK-013
  - Deliverable: Visual indicators for Brain/Memory/Tools activity

---

## Phase 2: Voice & Enhanced GUI (Weeks 5-8)

### 🎨 Voice Interface
- [ ] **TASK-015** Integrate faster-whisper for speech-to-text that already downloaded by me on models folders
  - Priority: High | Estimate: 8h
  - Dependencies: TASK-002
  - Deliverable: Real-time STT service with confidence scoring

- [ ] **TASK-016** Implement Piper text-to-speech
  - Priority: High | Estimate: 6h
  - Dependencies: TASK-002
  - Deliverable: TTS service with voice customization options

- [ ] **TASK-017** Add voice waveform visualization to GUI
  - Priority: Medium | Estimate: 4h
  - Dependencies: TASK-015, TASK-013
  - Deliverable: Real-time audio visualization in cosmic theme

### 🎨 GUI Enhancements
- [ ] **TASK-018** Implement agent thinking visualization
  - Priority: Medium | Estimate: 5h
  - Dependencies: TASK-013
  - Deliverable: Constellation patterns that pulse during processing

- [ ] **TASK-019** Create memory access indicators
  - Priority: Medium | Estimate: 3h
  - Dependencies: TASK-013
  - Deliverable: Starfield glow effects when accessing memory

- [ ] **TASK-020** Enhanced skills panel with tool status
  - Priority: Medium | Estimate: 4h
  - Dependencies: TASK-010, TASK-013
  - Deliverable: Dynamic tool availability and permission display

### 🔧 System Integration
- [ ] **TASK-021** Implement wake word detection
  - Priority: Medium | Estimate: 6h
  - Dependencies: TASK-015
  - Deliverable: Always-listening mode with configurable wake words

- [ ] **TASK-022** Add system tray functionality
  - Priority: Low | Estimate: 3h
  - Dependencies: GUI exists
  - Deliverable: Minimal footprint mode with quick access

---

## Phase 3: Advanced Memory System (Weeks 9-12)

### 💾 Memory Upgrades
- [ ] **TASK-023** Migrate to SQLite + embeddings storage
  - Priority: High | Estimate: 8h
  - Dependencies: TASK-007
  - Deliverable: Scalable memory system with semantic search

- [ ] **TASK-024** Implement sentence-transformers for embeddings
  - Priority: High | Estimate: 6h
  - Dependencies: TASK-023
  - Deliverable: Semantic similarity search for conversation context

- [ ] **TASK-025** Create context retrieval system
  - Priority: High | Estimate: 6h
  - Dependencies: TASK-024
  - Deliverable: Intelligent context selection for LLM prompts

- [ ] **TASK-026** Build conversation threading system
  - Priority: Medium | Estimate: 5h
  - Dependencies: TASK-023
  - Deliverable: Group related conversations and maintain topic threads

### 🎨 Memory Visualization
- [ ] **TASK-027** Create memory insights sidebar
  - Priority: Medium | Estimate: 5h
  - Dependencies: TASK-025, TASK-013
  - Deliverable: GUI panel showing recalled context and relevance

- [ ] **TASK-028** Implement context highlighting in chat
  - Priority: Low | Estimate: 3h
  - Dependencies: TASK-027
  - Deliverable: Visual indicators when agent uses past context

---

## Phase 4: Tool Expansion (Weeks 13-16)

### 🛠️ Application Integration
- [ ] **TASK-029** Kate editor integration
  - Priority: High | Estimate: 6h
  - Dependencies: TASK-010
  - Deliverable: Open files, create projects, basic editing commands

- [ ] **TASK-030** Firefox browser control
  - Priority: Medium | Estimate: 5h
  - Dependencies: TASK-010
  - Deliverable: Open URLs, bookmark management, tab control

- [ ] **TASK-031** Development environment helpers
  - Priority: High | Estimate: 8h
  - Dependencies: TASK-010
  - Deliverable: Git operations, build commands, terminal integration

### 🛠️ Media & File Management
- [ ] **TASK-032** Media player control (VLC/MPV)
  - Priority: Medium | Estimate: 4h
  - Dependencies: TASK-010
  - Deliverable: Play/pause/skip/volume control for media players

- [ ] **TASK-033** Dolphin file manager integration
  - Priority: Medium | Estimate: 5h
  - Dependencies: TASK-012
  - Deliverable: Navigate folders, file operations, smart organization

- [ ] **TASK-034** Smart file organization tool
  - Priority: Low | Estimate: 6h
  - Dependencies: TASK-033
  - Deliverable: AI-powered file categorization and cleanup

### 🔧 Security & Safety
- [ ] **TASK-035** Implement permission system
  - Priority: High | Estimate: 5h
  - Dependencies: TASK-010
  - Deliverable: Whitelist-based tool permissions with user approval

- [ ] **TASK-036** Create audit logging system
  - Priority: High | Estimate: 3h
  - Dependencies: TASK-035
  - Deliverable: Log all system interactions for security review

---

## Phase 5: Polish & Optimization (Weeks 17-20)

### 🚀 Performance & Optimization
- [ ] **TASK-037** Implement model caching and memory management
  - Priority: High | Estimate: 6h
  - Dependencies: TASK-004
  - Deliverable: Efficient LLM loading and memory usage optimization

- [ ] **TASK-038** Add background processing for non-blocking operations
  - Priority: Medium | Estimate: 5h
  - Dependencies: TASK-002
  - Deliverable: Async task queue for long-running operations

- [ ] **TASK-039** Optimize embedding computation and storage
  - Priority: Medium | Estimate: 4h
  - Dependencies: TASK-024
  - Deliverable: Fast embedding search with caching strategies

### 🎨 UI/UX Polish
- [ ] **TASK-040** Implement comprehensive error handling
  - Priority: High | Estimate: 4h
  - Dependencies: All major components
  - Deliverable: Graceful error recovery with user-friendly messages

- [ ] **TASK-041** Add accessibility features
  - Priority: Medium | Estimate: 5h
  - Dependencies: GUI components
  - Deliverable: Keyboard navigation, screen reader support, contrast options

- [ ] **TASK-042** Create onboarding and tutorial system
  - Priority: Medium | Estimate: 4h
  - Dependencies: GUI complete
  - Deliverable: First-time user experience and feature discovery

### 🚀 Packaging & Distribution
- [ ] **TASK-043** Create EndeavourOS/Arch package
  - Priority: High | Estimate: 6h
  - Dependencies: All core features complete
  - Deliverable: AUR package with proper dependencies

- [ ] **TASK-044** Write comprehensive documentation
  - Priority: High | Estimate: 8h
  - Dependencies: Feature complete
  - Deliverable: User guide, API docs, troubleshooting guide

- [ ] **TASK-045** Set up automated testing and CI/CD
  - Priority: Medium | Estimate: 6h
  - Dependencies: Core features
  - Deliverable: GitHub Actions for testing and release automation

---

## Critical Path Tasks

**Week 1-2 Priority:**
1. TASK-001, TASK-002 (Infrastructure)
2. TASK-004 (Ollama integration)
3. TASK-007 (Basic memory)
4. TASK-013 (GUI connection)

**Week 3-4 Priority:**
1. TASK-010, TASK-011 (Tools framework + app launcher)
2. TASK-005 (Context assembly)
3. TASK-015 (Speech-to-text)

**Blockers to Watch:**
- Ollama model performance on EndeavourOS
- Whisper.cpp compilation and optimization
- WebSocket stability between Electron and FastAPI

---

## Task Dependencies Graph

```
Foundation: 001 → 002 → 013 → 004 → 007 → 010
Voice: 015 → 016 → 017 → 021  
Memory: 007 → 023 → 024 → 025 → 027
Tools: 010 → 011, 012, 029, 030, 031
GUI: 013 → 014, 018, 019, 020
```

---

## Estimation Summary

- **Total Tasks:** 45
- **Total Estimated Hours:** ~235 hours
- **Average per Week:** ~12 hours
- **Critical Path:** ~28 hours (foundational tasks)

**Notes:**
- Estimates include testing and debugging time
- GUI enhancements may require additional design iteration
- Ollama integration complexity depends on model performance
- Tool development can be parallelized after framework completion
