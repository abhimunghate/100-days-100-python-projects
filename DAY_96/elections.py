from dataclasses import dataclass, field

@dataclass
class Election:
    id: int
    title: str
    candidates: dict[str, int]
    eligible_tokens: set[str]
    used_tokens: set[str] = field(default_factory=set)
    
class ElectionService:
    def __init__(self):
        self.elections = {
            101: Election(
                101,
                "Community Board Election",
                {"Ava Patel": 0, "Noah Smith": 0},
                {"TOKEN-A1", "TOKEN-B2", "TOKEN-C3"}
            )
        }
        
    def get(self, election_id):
        election = self.elections.get(election_id)
        if not election:
            raise LookupError("Election not found")
        return election
    
# Done