# PLANNING.md - Lyra AI Agent Development Plan

**Project:** Lyra AI Agent - Brain-Memory-Tools Architecture
**Version:** 2.0
**Planning Date:** August 2025
**Target Completion:** December 2025

---

## Executive Summary

Lyra AI Agent is a privacy-first desktop AI companion for EndeavourOS, built on a Brain-Memory-Tools architecture. The project spans 20 weeks across 5 phases, transitioning from the existing Electron GUI to a fully integrated AI agent capable of natural language system interaction while maintaining complete local data sovereignty.

---

## Project Phases Overview

| Phase | Duration | Focus | Key Deliverables | Success Criteria |
|-------|----------|-------|------------------|------------------|
| **Phase 1** | Weeks 1-4 | Core Foundation | Backend + Basic Brain + Simple Tools | Ollama integration working, basic chat functional |
| **Phase 2** | Weeks 5-8 | Voice & GUI Enhancement | STT/TTS + Visual enhancements | Voice commands working, enhanced starfield UI |
| **Phase 3** | Weeks 9-12 | Advanced Memory | Semantic search + Context retrieval | AI remembers past conversations accurately |
| **Phase 4** | Weeks 13-16 | Tool Expansion | App integration + System control | Natural language app control working |
| **Phase 5** | Weeks 17-20 | Polish & Deploy | Optimization + Packaging | AUR package ready, documentation complete |

---

## Detailed Phase Planning

### Phase 1: Core Foundation (Weeks 1-4)
**Goal:** Establish the Brain-Memory-Tools architecture foundation

#### Week 1: Infrastructure Setup
**Focus:** Backend architecture and project structure
- **Monday-Tuesday:** Project setup, Poetry configuration, basic FastAPI server
- **Wednesday-Thursday:** Ollama integration and basic LLM service 
- **Friday-Saturday:** Configuration management and API design
- **Sunday:** Testing and documentation

**Key Milestones:**
- ✅ FastAPI backend serving on localhost
- ✅ Ollama client successfully calling Gemma 3 4B
- ✅ Basic health check endpoints working

**Risks:** Ollama setup complexity on EndeavourOS, Gemma 3 model performance

#### Week 2: Brain Implementation
**Focus:** LLM integration and conversation handling
- **Monday-Tuesday:** Prompt template system and context assembly
- **Wednesday-Thursday:** Conversation flow and response generation
- **Friday-Saturday:** Basic memory storage (JSON-based)
- **Sunday:** Integration testing with existing GUI

**Key Milestones:**
- ✅ LLM generating coherent responses
- ✅ Conversation history stored and retrieved
- ✅ GUI can communicate with backend via WebSocket

**Risks:** Context length limitations, response quality with 4B model

#### Week 3: Basic Tools Framework  
**Focus:** Safe system interaction foundation
- **Monday-Tuesday:** Tool execution framework with Command pattern
- **Wednesday-Thursday:** Application launcher tool (Kate, Firefox, etc.)
- **Friday-Saturday:** File system interaction (safe, user-dir only)
- **Sunday:** Permission system and security testing

**Key Milestones:**
- ✅ Can launch applications from natural language
- ✅ Basic file operations working safely
- ✅ Permission whitelist preventing dangerous operations

**Risks:** Security vulnerabilities, cross-desktop environment compatibility

#### Week 4: Integration & Testing
**Focus:** Connect all components and stabilize
- **Monday-Tuesday:** GUI status indicators for Brain/Tools activity
- **Wednesday-Thursday:** End-to-end testing and bug fixes
- **Friday-Saturday:** Performance optimization and error handling
- **Sunday:** Phase 1 demo and retrospective

**Key Milestones:**
- ✅ Complete user workflow: text input → brain reasoning → tool execution → response
- ✅ GUI shows real-time status of agent activities
- ✅ System stable enough for daily use testing

### Phase 2: Voice & Enhanced GUI (Weeks 5-8)
**Goal:** Add voice capabilities and enhance visual feedback

#### Week 5: Speech-to-Text Integration
**Focus:** Real-time voice input with Whisper.cpp
- **Monday-Tuesday:** Whisper.cpp compilation and integration
- **Wednesday-Thursday:** Real-time STT service with streaming
- **Friday-Saturday:** Voice activity detection and confidence scoring
- **Sunday:** GUI microphone controls and visual feedback

**Key Milestones:**
- ✅ Voice commands converted to text accurately
- ✅ Real-time processing under 2 seconds
- ✅ GUI microphone button with proper state management

**Risks:** Whisper.cpp compilation issues, audio device compatibility

#### Week 6: Text-to-Speech Implementation
**Focus:** Natural voice responses with Piper
- **Monday-Tuesday:** Piper TTS integration and voice model selection
- **Wednesday-Thursday:** Voice customization and speed controls
- **Friday-Saturday:** Audio playback optimization and queue management
- **Sunday:** GUI audio visualization and settings

**Key Milestones:**
- ✅ Agent responds with natural speech
- ✅ Voice settings configurable by user
- ✅ Audio doesn't conflict with system sounds

#### Week 7: Enhanced Visual Feedback
**Focus:** Agent activity visualization in cosmic theme
- **Monday-Tuesday:** Constellation patterns for brain thinking states
- **Wednesday-Thursday:** Starfield glow effects for memory access
- **Friday-Saturday:** Tool execution animations and feedback
- **Sunday:** Voice waveform visualization during speech

**Key Milestones:**
- ✅ User can visually see when agent is "thinking"
- ✅ Memory access provides subtle visual feedback
- ✅ Tool execution shows clear status and completion

#### Week 8: Wake Word & System Integration
**Focus:** Always-listening mode and system tray
- **Monday-Tuesday:** Wake word detection implementation
- **Wednesday-Thursday:** System tray functionality and minimal mode
- **Friday-Saturday:** Hotkey management and background operation
- **Sunday:** Phase 2 integration testing and demo

**Key Milestones:**
- ✅ "Hey Lyra" or custom wake word activates assistant
- ✅ Runs efficiently in background with system tray
- ✅ Complete voice workflow: wake word → command → voice response

### Phase 3: Advanced Memory System (Weeks 9-12)
**Goal:** Implement semantic memory with context retrieval

#### Week 9: Memory Architecture Migration
**Focus:** SQLite + embeddings foundation
- **Monday-Tuesday:** Database schema design and migration from JSON
- **Wednesday-Thursday:** Sentence-transformers integration for embeddings
- **Friday-Saturday:** Batch embedding computation for existing conversations
- **Sunday:** Performance testing and optimization

**Key Milestones:**
- ✅ All conversation history migrated to SQLite
- ✅ Embeddings generated for semantic search
- ✅ Query performance under 500ms for memory searches

#### Week 10: Semantic Search Implementation
**Focus:** Intelligent context retrieval
- **Monday-Tuesday:** Vector similarity search implementation
- **Wednesday-Thursday:** Context ranking and relevance scoring
- **Friday-Saturday:** Multi-turn conversation understanding
- **Sunday:** Memory retrieval optimization and caching

**Key Milestones:**
- ✅ Agent finds relevant past conversations by meaning
- ✅ Context retrieval improves response quality
- ✅ Memory searches don't slow down conversations

#### Week 11: Context Assembly & Threading
**Focus:** Conversation continuity and topic tracking
- **Monday-Tuesday:** Conversation threading and topic detection
- **Wednesday-Thursday:** Context assembly for LLM prompts
- **Friday-Saturday:** Long-term memory pattern recognition
- **Sunday:** User preference learning and adaptation

**Key Milestones:**
- ✅ Agent maintains context across multiple sessions
- ✅ Related conversations grouped intelligently
- ✅ Agent learns and adapts to user preferences

#### Week 12: Memory Visualization
**Focus:** GUI for memory insights and context awareness
- **Monday-Tuesday:** Memory insights sidebar development
- **Wednesday-Thursday:** Context highlighting in chat interface
- **Friday-Saturday:** Memory search and exploration features
- **Sunday:** Phase 3 integration testing and user feedback

**Key Milestones:**
- ✅ Users can see what context agent is using
- ✅ Memory insights help users understand agent decisions
- ✅ Memory system enhances rather than slows experience

### Phase 4: Tool Expansion (Weeks 13-16)
**Goal:** Comprehensive EndeavourOS application integration

#### Week 13: Development Environment Integration
**Focus:** Code editor and development tools
- **Monday-Tuesday:** Kate editor integration (open files, projects)
- **Wednesday-Thursday:** Git operations through natural language
- **Friday-Saturday:** Terminal integration and build command execution
- **Sunday:** VS Code integration and development workflow testing

**Key Milestones:**
- ✅ "Open my Python project in Kate" works correctly
- ✅ "Commit these changes with message X" executes properly
- ✅ Development workflows feel natural and safe

#### Week 14: Browser & Communication Tools
**Focus:** Web browser and communication integration
- **Monday-Tuesday:** Firefox control (tabs, bookmarks, navigation)
- **Wednesday-Thursday:** URL opening and web search integration
- **Friday-Saturday:** Email client basic integration (if applicable)
- **Sunday:** Communication workflow testing

**Key Milestones:**
- ✅ "Open GitHub in Firefox" works reliably
- ✅ Bookmark management through conversation
- ✅ Web-related tasks feel integrated

#### Week 15: Media & File Management
**Focus:** Multimedia and file organization
- **Monday-Tuesday:** VLC/MPV media player control
- **Wednesday-Thursday:** Dolphin file manager integration
- **Friday-Saturday:** Smart file organization and cleanup tools
- **Sunday:** Media and file workflow testing

**Key Milestones:**
- ✅ "Play some music" finds and plays audio files
- ✅ "Organize my Downloads folder" works intelligently
- ✅ File operations maintain safety boundaries

#### Week 16: Security & Permission Refinement
**Focus:** Security hardening and user experience
- **Monday-Tuesday:** Permission system enhancement and user approval flows
- **Wednesday-Thursday:** Audit logging and security monitoring
- **Friday-Saturday:** Tool usage analytics and success rate tracking
- **Sunday:** Phase 4 security review and penetration testing

**Key Milestones:**
- ✅ All tool operations logged and auditable
- ✅ User can grant/revoke permissions easily
- ✅ No security vulnerabilities in tool execution

### Phase 5: Polish & Deployment (Weeks 17-20)
**Goal:** Production-ready release and distribution

#### Week 17: Performance Optimization
**Focus:** Resource efficiency and speed improvements
- **Monday-Tuesday:** Model loading optimization and memory management
- **Wednesday-Thursday:** Embedding computation caching and batching
- **Friday-Saturday:** Background processing and async operations
- **Sunday:** Performance benchmarking and bottleneck identification

**Key Milestones:**
- ✅ Memory usage under 6GB under normal load
- ✅ Response times consistently under 3 seconds
- ✅ CPU usage reasonable during background operation

#### Week 18: User Experience Polish
**Focus:** Accessibility, error handling, and onboarding
- **Monday-Tuesday:** Comprehensive error handling and recovery
- **Wednesday-Thursday:** Accessibility features (keyboard nav, screen reader)
- **Friday-Saturday:** Onboarding tutorial and feature discovery
- **Sunday:** User experience testing and feedback incorporation

**Key Milestones:**
- ✅ Graceful handling of all error conditions
- ✅ Accessible to users with disabilities
- ✅ New users can discover features naturally

#### Week 19: Documentation & Testing
**Focus:** Comprehensive documentation and automated testing
- **Monday-Tuesday:** User documentation and troubleshooting guides
- **Wednesday-Thursday:** API documentation and developer guides
- **Friday-Saturday:** Automated testing suite and CI/CD setup
- **Sunday:** Beta testing and feedback collection

**Key Milestones:**
- ✅ Complete user manual available
- ✅ Developer documentation for extensions
- ✅ Automated tests cover critical functionality

#### Week 20: Packaging & Release
**Focus:** Distribution and community launch
- **Monday-Tuesday:** AUR package creation and testing
- **Wednesday-Thursday:** GitHub release preparation and asset building
- **Friday-Saturday:** Community announcement and documentation website
- **Sunday:** Official launch and post-release monitoring

**Key Milestones:**
- ✅ Lyra available via AUR package manager
- ✅ GitHub releases with proper versioning
- ✅ Community can discover and install easily

---

## Resource Planning

### Development Environment Requirements
- **Hardware:** 16GB RAM, 8-core CPU, 20GB free disk space
- **Software:** EndeavourOS, Python 3.11+, Node.js 18+, Ollama with Gemma 3 4B
- **Tools:** VS Code/Kate, Git, Docker (for testing), Postman/Insomnia

### Team Structure (Solo Developer)
- **Week Time Commitment:** ~12 hours (flexible, can be adjusted)
- **Peak Hours:** Weeks 9-12 (Memory system), Weeks 17-20 (Polish)
- **Buffer Time:** Built into each phase for unexpected complexity

### Dependencies & External Factors
- **Ollama Stability:** Critical for Brain functionality
- **Model Performance:** Gemma 3 4B may need optimization
- **EndeavourOS Updates:** Could affect desktop integrations
- **Community Feedback:** May influence feature priorities

---

## Risk Management Strategy

### High-Risk Items
1. **Model Performance:** 4B parameter model may be insufficient
   - **Mitigation:** Test extensively, consider model quantization options
   - **Backup Plan:** Support for multiple model backends

2. **Memory System Scalability:** Embedding storage may become slow
   - **Mitigation:** Implement efficient indexing and caching
   - **Backup Plan:** Hybrid memory approach with different storage tiers

3. **Security Vulnerabilities:** Tool system could be exploited
   - **Mitigation:** Extensive security testing, conservative permissions
   - **Backup Plan:** Sandboxed execution environment

### Medium-Risk Items
- **Cross-DE Compatibility:** Focus on KDE but test others
- **Voice Recognition Accuracy:** May need fine-tuning for user's accent
- **Resource Consumption:** Monitor and optimize throughout development

### Low-Risk Items  
- **GUI Polish:** Existing design is solid foundation
- **Documentation:** Can be done incrementally
- **Community Adoption:** Good concept should find users

---

## Success Metrics & KPIs

### Technical Metrics
- **Response Time:** 95% of queries under 3 seconds
- **Memory Usage:** Peak usage under 6GB RAM
- **Accuracy:** 85% task completion rate for common workflows
- **Uptime:** 99.5% crash-free operation during 8-hour usage

### User Experience Metrics
- **Onboarding:** New users complete first successful task within 5 minutes
- **Daily Usage:** Beta testers use 5+ features per day
- **Satisfaction:** Net Promoter Score above 70
- **Support:** Less than 10% of users need installation help

### Development Metrics
- **Code Quality:** 80%+ test coverage for critical components
- **Documentation:** All API endpoints and user features documented
- **Community:** 50+ GitHub stars, 10+ community contributions
- **Distribution:** Successful AUR package with proper dependencies

---

## Milestone Decision Points

### End of Phase 1 (Week 4)
**Go/No-Go Decision:** Continue to voice interface development
- **Criteria:** Basic chat working, tools executing safely, GUI connected
- **Risk Assessment:** If model performance inadequate, consider alternatives

### End of Phase 2 (Week 8)  
**Go/No-Go Decision:** Proceed with advanced memory system
- **Criteria:** Voice commands working reliably, GUI enhancements complete
- **Risk Assessment:** If voice accuracy poor, focus on text interface

### End of Phase 3 (Week 12)
**Go/No-Go Decision:** Expand tool integrations vs. polish existing
- **Criteria:** Memory system providing clear value, context retrieval working
- **Risk Assessment:** If memory too complex, simplify before tool expansion

### End of Phase 4 (Week 16)
**Go/No-Go Decision:** Final polish and release preparation
- **Criteria:** Key applications integrated, security model solid
- **Risk Assessment:** If major security issues, delay release for fixes

---

## Future Roadmap (Beyond v2.0)

### Version 2.1 (Q1 2026)
- Plugin API for community extensions
- Additional language model support
- Mobile companion app (Android)

### Version 2.2 (Q2 2026)  
- Advanced calendar and email integration
- Multi-user support on same system
- Voice personality customization

### Version 3.0 (Q3 2026)
- Multi-modal input (vision, document processing)
- Advanced workflow automation
- Enterprise/team collaboration features

---

## Communication Plan

### Weekly Updates
- **Monday:** Week planning and task prioritization  
- **Friday:** Progress review and blocker identification
- **Sunday:** Documentation updates and community engagement

### Phase Reviews
- End-of-phase demos and retrospectives
- Community feedback collection and incorporation
- Technical debt assessment and planning

### Community Engagement
- Regular development updates on GitHub
- Beta testing program for EndeavourOS community
- Documentation and tutorial creation

---

## Conclusion

This planning document provides a comprehensive roadmap for developing Lyra AI Agent from the existing GUI foundation to a fully-featured AI companion. The phased approach allows for iterative development, risk mitigation, and community feedback incorporation while maintaining focus on the core Brain-Memory-Tools architecture.

The 20-week timeline is ambitious but achievable for a solo developer with the existing GUI foundation and clear technical direction. Regular milestone reviews and flexible scheduling will help accommodate unexpected challenges and opportunities for improvement.