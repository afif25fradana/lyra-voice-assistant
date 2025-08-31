import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from fastapi import APIRouter, WebSocket
from brain.llm_service import LLMService
import json

router = APIRouter(prefix="/api/v1")

# Initialize the LLM service
llm_service = LLMService()

@router.get("/health")
async def health_check():
    """Health check endpoint for the API"""
    return {"status": "healthy", "service": "Lyra API"}

@router.post("/chat")
async def chat_completion(request: dict):
    """
    Generate a chat completion response
    
    Expected request format:
    {
        "prompt": "User's message",
        "system_prompt": "Optional system prompt"
    }
    """
    prompt = request.get("prompt", "")
    system_prompt = request.get("system_prompt")
    
    if not prompt:
        return {"error": "Prompt is required"}
    
    response = await llm_service.generate_response(prompt, system_prompt)
    return {"response": response}

@router.websocket("/ws/chat")
async def chat_websocket(websocket: WebSocket):
    """WebSocket endpoint for real-time chat"""
    print("WebSocket connection attempt")
    await websocket.accept()
    print("WebSocket connection accepted")
    
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            print(f"Received data: {data}")
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
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()
        print("WebSocket connection closed")