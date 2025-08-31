import asyncio
from brain.llm_service import LLMService

async def test():
    llm = LLMService()
    response = await llm.generate_response('Hello, how are you?')
    print(f'Response: {response}')

if __name__ == "__main__":
    asyncio.run(test())