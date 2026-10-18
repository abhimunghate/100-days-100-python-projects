from datetime import datetime, timezone

class TicketService:
    def __init__(self):
        self.tickets = []
        
    def create(self, message, reason):
        ticket = {
            "ticket_id": f"TKT-{len(self.tickets)+1:04}",
            "message": message,
            "reason": reason,
            "status": "open",
            "created_at": datetime.now(timezone.utc).isoformat()
        }
        self.tickets.append(ticket)
        return ticket
    
# Done