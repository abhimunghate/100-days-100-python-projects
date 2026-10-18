# This is Day 99 project : AI-Powered Customer Service Chatbot

import json
from chatbot import SupportChatbot
from knowledge_base import ARTICLES
from tickets import TicketService

def show(message, data):
    print(f"\nCUSTOMER {message}\nBOT RESPONSE\n{json.dumps(data, indent=2)}")
    
def main():
    print("Day 99 - AI-Powered Customer Service Chatbot")
    tickets = TicketService()
    bot = SupportChatbot(ARTICLES, tickets)
    for message in [
        "Where can I track my order status?",
        "I need to return an item for a refund.",
        "My device arrived with a cracked screen."
    ]:
        show(message, bot.reply(message))
        
if __name__ == "__main__":
    main()
    
# Done