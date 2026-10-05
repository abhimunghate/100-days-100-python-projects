# This is Day 86 project : Chat Application

import json
from conversations import ConversationService
from messages import MessageService

def show(action, result, status=200):
    print(f"\nREQUEST {action}\nRESPONSE {status}\n{json.dumps(result, indent=2)}")
    
def main():
    print("Day 86 - Chat Application")
    conversations = ConversationService()
    messages = MessageService(conversations)
    
    chat = conversations.create(["Ava", "Noah"])
    show("CREATE CONVERSATION", chat.to_dict(), 201)
    show("SEND MESSAGE", messages.send(chat.id, "Ava", "Are we still meeting at 3 PM?"), 201)
    show("SEND MESSAGE", messages.send(chat.id, "Noah", "Yes, see you then."), 201)
    show("GET HISTORY", chat.to_dict())
    
if __name__ == "__main__":
    main()
    
# Done