from abc import ABC, abstractmethod
from typing import Dict, Any, List
import subprocess
import os

class Tool(ABC):
    """Abstract base class for all tools"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    @abstractmethod
    async def execute(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the tool with given parameters
        
        Args:
            parameters: Tool-specific parameters
            
        Returns:
            Result of the tool execution
        """
        pass

class ToolExecutor:
    """Executes tools safely with permission checking"""
    
    def __init__(self):
        self.tools: Dict[str, Tool] = {}
        self.permissions: Dict[str, bool] = {}
    
    def register_tool(self, tool: Tool):
        """Register a tool with the executor"""
        self.tools[tool.name] = tool
        # By default, tools are not permitted
        self.permissions[tool.name] = False
    
    def grant_permission(self, tool_name: str):
        """Grant permission to execute a tool"""
        if tool_name in self.tools:
            self.permissions[tool_name] = True
    
    def revoke_permission(self, tool_name: str):
        """Revoke permission to execute a tool"""
        if tool_name in self.tools:
            self.permissions[tool_name] = False
    
    async def execute_tool(self, tool_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a tool safely
        
        Args:
            tool_name: Name of the tool to execute
            parameters: Parameters for the tool
            
        Returns:
            Result of the tool execution
        """
        # Check if tool exists
        if tool_name not in self.tools:
            return {"error": f"Tool '{tool_name}' not found"}
        
        # Check if tool is permitted
        if not self.permissions.get(tool_name, False):
            return {"error": f"Permission denied for tool '{tool_name}'"}
        
        # Execute the tool
        try:
            result = await self.tools[tool_name].execute(parameters)
            return result
        except Exception as e:
            return {"error": f"Error executing tool '{tool_name}': {str(e)}"}

class ApplicationLauncher(Tool):
    """Tool for launching applications"""
    
    def __init__(self):
        super().__init__(
            name="app_launcher",
            description="Launch desktop applications"
        )
    
    async def execute(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        app_name = parameters.get("app_name")
        
        if not app_name:
            return {"error": "app_name parameter is required"}
        
        try:
            # Attempt to launch the application
            subprocess.Popen([app_name])
            return {
                "status": "success",
                "message": f"Launched {app_name}"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Failed to launch {app_name}: {str(e)}"
            }

# Example usage
if __name__ == "__main__":
    # Test the tool framework
    executor = ToolExecutor()
    
    # Register a tool
    launcher = ApplicationLauncher()
    executor.register_tool(launcher)
    
    # Grant permission
    executor.grant_permission("app_launcher")
    
    # Execute the tool
    import asyncio
    async def test_tool():
        result = await executor.execute_tool("app_launcher", {"app_name": "kate"})
        print(f"Tool result: {result}")
    
    asyncio.run(test_tool())