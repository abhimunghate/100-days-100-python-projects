from datetime import datetime, timezone

class MessageService:
    def __init__(self, conversations):
        self.conversations = conversations
        
    def send(self, conversation_id, sender, text):
        chat = self.conversations.get(conversation_id)
        if sender not in chat.participants:
            raise PermissionError("Sender is not a participant")
        if not text.strip():
            raise ValueError("Message cannot be empty")
        
        message = {"id": f"MSG-{len(chat.messages)+1:04}", "sender": sender, "text": text, "sent_at": datetime.now(timezone.utc).isoformat()}
        chat.messages.append(message)
        return message
    
# Done