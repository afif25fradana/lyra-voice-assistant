import json
import os
from typing import List, Dict, Any, Optional
from datetime import datetime
from pathlib import Path

class MemoryManager:
    """Manages conversation history and user preferences in JSON format"""
    
    def __init__(self, storage_path: str = "../memory/conversations.json"):
        # Convert to absolute path if it's a relative path
        if not os.path.isabs(storage_path):
            storage_path = os.path.join(os.path.dirname(__file__), storage_path)
        
        self.storage_path = storage_path
        self._ensure_storage_path()
        self.conversations = self._load_conversations()
    
    def _ensure_storage_path(self):
        """Ensure the storage path exists"""
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        if not os.path.exists(self.storage_path):
            with open(self.storage_path, 'w') as f:
                json.dump([], f)
    
    def _load_conversations(self) -> List[Dict]:
        """Load conversations from storage"""
        try:
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _save_conversations(self):
        """Save conversations to storage"""
        with open(self.storage_path, 'w') as f:
            json.dump(self.conversations, f, indent=2)
    
    def create_conversation(self, conversation_id: Optional[str] = None) -> str:
        """
        Create a new conversation
        
        Args:
            conversation_id: Optional ID for the conversation
            
        Returns:
            The conversation ID
        """
        if not conversation_id:
            conversation_id = datetime.now().isoformat()
        
        conversation = {
            "id": conversation_id,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "messages": []
        }
        
        self.conversations.append(conversation)
        self._save_conversations()
        return conversation_id
    
    def add_message(self, conversation_id: str, role: str, content: str):
        """
        Add a message to a conversation
        
        Args:
            conversation_id: ID of the conversation
            role: Role of the message sender (user, assistant, system)
            content: Content of the message
        """
        conversation = self._get_conversation(conversation_id)
        if not conversation:
            # Create conversation if it doesn't exist
            self.create_conversation(conversation_id)
            conversation = self._get_conversation(conversation_id)
            
            # Ensure conversation is not None after creation
            if not conversation:
                raise RuntimeError(f"Failed to create or retrieve conversation with ID: {conversation_id}")
        
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        
        conversation["messages"].append(message)
        conversation["updated_at"] = datetime.now().isoformat()
        self._save_conversations()
    
    def get_conversation(self, conversation_id: str) -> Optional[Dict]:
        """
        Get a conversation by ID
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            The conversation data or None if not found
        """
        return self._get_conversation(conversation_id)
    
    def _get_conversation(self, conversation_id: str) -> Optional[Dict]:
        """Internal method to get a conversation by ID"""
        for conversation in self.conversations:
            if conversation["id"] == conversation_id:
                return conversation
        return None
    
    def get_conversation_history(self, conversation_id: str, limit: Optional[int] = None) -> List[Dict]:
        """
        Get the message history for a conversation
        
        Args:
            conversation_id: ID of the conversation
            limit: Optional limit on number of messages to return
            
        Returns:
            List of messages
        """
        conversation = self._get_conversation(conversation_id)
        if not conversation:
            return []
        
        messages = conversation["messages"]
        if limit:
            messages = messages[-limit:]
        return messages
    
    def delete_conversation(self, conversation_id: str) -> bool:
        """
        Delete a conversation
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            True if deleted, False if not found
        """
        conversation = self._get_conversation(conversation_id)
        if not conversation:
            return False
        
        self.conversations.remove(conversation)
        self._save_conversations()
        return True

# Example usage
if __name__ == "__main__":
    # Test the memory manager
    memory = MemoryManager()
    
    # Create a new conversation
    conv_id = memory.create_conversation()
    print(f"Created conversation: {conv_id}")
    
    # Add messages
    memory.add_message(conv_id, "user", "Hello, how are you?")
    memory.add_message(conv_id, "assistant", "I'm doing well, thank you for asking!")
    
    # Retrieve conversation
    conversation = memory.get_conversation(conv_id)
    print(f"Conversation: {conversation}")