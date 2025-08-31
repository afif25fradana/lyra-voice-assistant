from memory.storage import MemoryManager

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