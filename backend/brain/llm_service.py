from ollama import AsyncClient
from typing import List, Dict, Any, Optional
import asyncio

class LLMService:
    """LLM service for interacting with Ollama models"""
    
    def __init__(self, model_name: str = "gemma3:4b-it-q4_K_M"):
        self.model_name = model_name
        self.client = AsyncClient()
    
    async def generate_response(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """
        Generate a response from the LLM
        
        Args:
            prompt: The user's prompt
            system_prompt: Optional system prompt to guide the model
            
        Returns:
            The generated response text
        """
        messages = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
            
        messages.append({"role": "user", "content": prompt})
        
        try:
            response = await self.client.chat(
                model=self.model_name,
                messages=messages
            )
            return response['message']['content']
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Sorry, I encountered an error while processing your request."
    
    async def stream_response(self, prompt: str, system_prompt: Optional[str] = None):
        """
        Stream a response from the LLM
        
        Args:
            prompt: The user's prompt
            system_prompt: Optional system prompt to guide the model
            
        Yields:
            Chunks of the response as they are generated
        """
        messages = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
            
        messages.append({"role": "user", "content": prompt})
        
        try:
            async for chunk in await self.client.chat(
                model=self.model_name,
                messages=messages,
                stream=True
            ):
                yield chunk['message']['content']
        except Exception as e:
            print(f"Error streaming response: {e}")
            yield "Sorry, I encountered an error while processing your request."

# Example usage
if __name__ == "__main__":
    # Test the LLM service
    async def test_llm():
        llm = LLMService()
        response = await llm.generate_response("Hello, how are you?")
        print(f"Response: {response}")
    
    asyncio.run(test_llm())