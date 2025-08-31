import sys
import os
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from api.routes import router as api_router

app = FastAPI(title="Lyra AI Agent", description="Privacy-first desktop AI companion")

# Include API routes with proper prefix
app.include_router(api_router)

# Add a direct WebSocket route for debugging
from fastapi import WebSocket
import json
from brain.llm_service import LLMService

llm_service = LLMService()

@app.websocket("/api/v1/ws/chat")
async def chat_websocket(websocket: WebSocket):
    """Direct WebSocket endpoint for real-time chat"""
    print("Direct WebSocket connection attempt")
    await websocket.accept()
    print("Direct WebSocket connection accepted")
    
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            print(f"Direct WebSocket received data: {data}")
            message_data = json.loads(data)
            
            prompt = message_data.get("prompt", "")
            system_prompt = message_data.get("system_prompt")
            
            if prompt:
                # Stream the response back to the client
                async for chunk in llm_service.stream_response(prompt, system_prompt):
                    await websocket.send_text(json.dumps({"type": "chunk", "content": chunk}))
                
                # Send end of response signal
                await websocket.send_text(json.dumps({"type": "end"}))
            else:
                await websocket.send_text(json.dumps({"type": "error", "content": "Prompt is required"}))
    except Exception as e:
        print(f"Direct WebSocket error: {e}")
    finally:
        await websocket.close()
        print("Direct WebSocket connection closed")

# Health check endpoint
@app.get("/health")
async def health_check():
    """Basic health check endpoint"""
    return {"status": "healthy", "service": "Lyra AI Agent"}

# Serve static files from the gui directory
# The html=True parameter allows serving index.html and other static files
app.mount("/", StaticFiles(directory="../gui", html=True), name="gui")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5252)