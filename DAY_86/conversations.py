from dataclasses import asdict, dataclass, field
from uuid import uuid4

@dataclass
class Conversation:
    id: str
    participants: list[str]
    messages: list = field(default_factory=list)
    
    def to_dict(self):
        return asdict(self)
    
class ConversationService:
    def __init__(self):
        self.conversations = {}
        
    def create(self, participants):
        if len(set(participants)) < 2:
            raise ValueError("Two participants are required")
        
        chat = Conversation(f"CHAT-{uuid4().hex[:8].upper()}", participants)
        self.conversations[chat.id] = chat
        return chat
    
    def get(self, conversation_id):
        chat = self.conversations.get(conversation_id)
        if not chat:
            raise LookupError("Conversation not found")
        return chat
    
# Done