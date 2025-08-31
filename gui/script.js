// script.js - Frontend logic for Lyra AI Agent

class LyraClient {
    constructor() {
        this.ws = null;
        this.isConnected = false;
        this.initializeElements();
        this.attachEventListeners();
        this.createStarfield(); // Add starfield generation
        this.connect();
        this.populateSkills();
    }

    initializeElements() {
        this.statusDot = document.getElementById('status-dot');
        this.statusText = document.getElementById('status-text');
        this.chatHistory = document.getElementById('chat-history');
        this.userInput = document.getElementById('user-input');
        this.sendButton = document.getElementById('send-button');
        this.micButton = document.getElementById('mic-button');
    }

    // Add starfield generation
    createStarfield() {
        const starfield = document.getElementById('starfield');
        const starCount = 100;
        
        for (let i = 0; i < starCount; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            
            // Random size
            const size = Math.random();
            if (size < 0.5) star.classList.add('small');
            else if (size < 0.8) star.classList.add('medium');
            else star.classList.add('large');
            
            // Random position
            star.style.left = Math.random() * 100 + '%';
            star.style.top = Math.random() * 100 + '%';
            
            // Random animation delay
            star.style.animationDelay = Math.random() * 3 + 's';
            
            starfield.appendChild(star);
        }
    }

    attachEventListeners() {
        this.sendButton.addEventListener('click', () => this.sendMessage());
        this.userInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.sendMessage();
            }
        });
    }

    connect() {
        try {
            // Connect to the WebSocket endpoint on port 5252
            this.ws = new WebSocket('ws://localhost:5252/api/v1/ws/chat');
            
            this.ws.onopen = () => {
                this.isConnected = true;
                this.updateStatus('connected', 'Connected');
                this.addMessage('assistant', 'Hello! I\'m Lyra, your AI assistant. How can I help you today?');
            };
            
            this.ws.onmessage = (event) => {
                const data = JSON.parse(event.data);
                if (data.type === 'chunk') {
                    // Handle streaming response
                    this.addStreamingChunk(data.content);
                } else if (data.type === 'end') {
                    // End of streaming response
                    this.endStreaming();
                } else if (data.type === 'error') {
                    // Handle error
                    this.addMessage('assistant', `Error: ${data.content}`);
                }
            };
            
            this.ws.onclose = () => {
                this.isConnected = false;
                this.updateStatus('disconnected', 'Disconnected');
                // Try to reconnect after 5 seconds
                setTimeout(() => this.connect(), 5000);
            };
            
            this.ws.onerror = (error) => {
                console.error('WebSocket error:', error);
                this.updateStatus('error', 'Connection Error');
            };
        } catch (error) {
            console.error('Connection error:', error);
            this.updateStatus('error', 'Connection Failed');
        }
    }

    updateStatus(status, text) {
        this.statusDot.className = `status-dot ${status}`;
        this.statusText.textContent = text;
    }

    sendMessage() {
        const message = this.userInput.value.trim();
        if (!message || !this.isConnected) return;

        // Add user message to chat
        this.addMessage('user', message);
        
        // Clear input
        this.userInput.value = '';
        
        // Create a new response container for streaming
        this.createResponseContainer();

        // Send message to backend
        this.ws.send(JSON.stringify({
            prompt: message
        }));
    }

    addMessage(role, content) {
        const messageDiv = document.createElement('div');
        // Use the new class names for chat bubbles
        messageDiv.className = `message ${role}-message`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.textContent = content;
        
        messageDiv.appendChild(contentDiv);
        this.chatHistory.appendChild(messageDiv);
        
        // Scroll to bottom
        this.chatHistory.scrollTop = this.chatHistory.scrollHeight;
    }

    createResponseContainer() {
        this.currentResponseDiv = document.createElement('div');
        // Use the new class name for AI messages
        this.currentResponseDiv.className = 'message assistant-message';
        
        this.currentContentDiv = document.createElement('div');
        this.currentContentDiv.className = 'message-content';
        this.currentContentDiv.textContent = '';
        
        this.currentResponseDiv.appendChild(this.currentContentDiv);
        this.chatHistory.appendChild(this.currentResponseDiv);
        
        // Scroll to bottom
        this.chatHistory.scrollTop = this.chatHistory.scrollHeight;
    }

    addStreamingChunk(content) {
        if (!this.currentContentDiv) {
            this.createResponseContainer();
        }
        
        this.currentContentDiv.textContent += content;
        
        // Scroll to bottom
        this.chatHistory.scrollTop = this.chatHistory.scrollHeight;
    }

    endStreaming() {
        this.currentResponseDiv = null;
        this.currentContentDiv = null;
    }

    populateSkills() {
        const skillsList = document.getElementById('skills-list');
        const skills = [
            { name: 'Web Search', description: 'Search the web for information', icon: 'search' },
            { name: 'File Management', description: 'Organize and manage files', icon: 'folder' },
            { name: 'Application Launch', description: 'Open applications and programs', icon: 'rocket' },
            { name: 'System Control', description: 'Control system settings', icon: 'cog' },
            { name: 'Development Tools', description: 'Code editing and compilation', icon: 'code' },
            { name: 'Media Control', description: 'Play and control media', icon: 'play' }
        ];

        skillsList.innerHTML = '';
        skills.forEach(skill => {
            const skillDiv = document.createElement('div');
            skillDiv.className = 'skill-item';
            skillDiv.innerHTML = `
                <div class="skill-name">
                    <div class="skill-icon">
                        <i class="fas fa-${skill.icon}"></i>
                    </div>
                    ${skill.name}
                </div>
                <div class="skill-description">${skill.description}</div>
            `;
            skillsList.appendChild(skillDiv);
        });
    }
}

// Initialize the client when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new LyraClient();
});