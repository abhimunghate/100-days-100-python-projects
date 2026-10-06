from dataclasses import dataclass, field

@dataclass
class Poll:
    id: int
    question: str
    options: dict[str, int]
    voters: set[str] = field(default_factory=set)
    
class PollService:
    def __init__(self):
        self.polls = {101: Poll(101, "What should we build next?", {"API": 0, "Automation": 0, "Data": 0})}
        
    def get(self, poll_id):
        poll = self.polls.get(poll_id)
        if not poll:
            raise LookupError("Poll not found")
        return poll
    
# Done