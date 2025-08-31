import asyncio
from tools.executor import ToolExecutor, ApplicationLauncher

async def test():
    # Test the tool framework
    executor = ToolExecutor()
    
    # Register a tool
    launcher = ApplicationLauncher()
    executor.register_tool(launcher)
    
    # Grant permission
    executor.grant_permission("app_launcher")
    
    # Execute the tool
    result = await executor.execute_tool("app_launcher", {"app_name": "echo"})
    print(f"Tool result: {result}")

if __name__ == "__main__":
    asyncio.run(test())