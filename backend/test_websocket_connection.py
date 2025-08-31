import asyncio
import websockets
import json

async def test_websocket():
    uri = "ws://localhost:5252/api/v1/ws/chat"
    try:
        async with websockets.connect(uri) as websocket:
            print("✅ Connected to WebSocket")
            
            # Send a message
            message = {
                "prompt": "Hello, how are you?"
            }
            await websocket.send(json.dumps(message))
            print("📤 Sent message")
            
            # Receive response
            while True:
                try:
                    response = await websocket.recv()
                    data = json.loads(response)
                    print(f"📥 Received: {data}")
                    
                    if data.get("type") == "end":
                        break
                except websockets.exceptions.ConnectionClosed:
                    break
                    
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_websocket())