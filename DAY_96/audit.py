from datetime import datetime, timezone
from hashlib import sha256

class AuditLog:
    def __init__(self):
        self.events = []
        
    def record(self, election_id, token, candidate):
        event = {
            "election_id": election_id,
            "voter_hash": sha256(token.encode()).hexdigest()[:12],
            "candidate": candidate,
            "recorded_at": datetime.now(timezone.utc).isoformat()
        }
        self.events.append(event)
        return event
    
# Done