import asyncio
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from brain.llm_service import LLMService
from memory.storage import MemoryManager
from tools.executor import ToolExecutor, ApplicationLauncher

async def test_all_components():
    print("🧪 Testing all Lyra components...\n")
    
    # Test 1: LLM Service
    print("1. Testing LLM Service...")
    try:
        llm = LLMService()
        response = await llm.generate_response("Hello, how are you?")
        print(f"   ✅ LLM Response: {response[:50]}...")
    except Exception as e:
        print(f"   ❌ LLM Error: {e}")
        return False
    
    # Test 2: Memory Manager
    print("\n2. Testing Memory Manager...")
    try:
        memory = MemoryManager("../memory/test_memory.json")
        conv_id = memory.create_conversation()
        memory.add_message(conv_id, "user", "Hello, how are you?")
        memory.add_message(conv_id, "assistant", "I'm doing well, thank you!")
        conversation = memory.get_conversation(conv_id)
        if conversation:
            print(f"   ✅ Memory Test: Created conversation with {len(conversation['messages'])} messages")
        else:
            print("   ❌ Memory Error: Failed to retrieve conversation")
            return False
    except Exception as e:
        print(f"   ❌ Memory Error: {e}")
        return False
    
    # Test 3: Tool Executor
    print("\n3. Testing Tool Executor...")
    try:
        executor = ToolExecutor()
        launcher = ApplicationLauncher()
        executor.register_tool(launcher)
        executor.grant_permission("app_launcher")
        result = await executor.execute_tool("app_launcher", {"app_name": "echo"})
        print(f"   ✅ Tool Test: {result['status']} - {result['message']}")
    except Exception as e:
        print(f"   ❌ Tool Error: {e}")
        return False
    
    print("\n🎉 All components are working correctly!")
    return True

if __name__ == "__main__":
    success = asyncio.run(test_all_components())
    sys.exit(0 if success else 1)