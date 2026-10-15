class VotingService:
    def __init__(self, elections, audit):
        self.elections, self.audit = elections, audit
        
    def cast(self, election_id, token, candidate):
        election = self.elections.get(election_id)
        if token not in election.eligible_tokens:
            raise PermissionError("Invalid voter token")
        if token in election.used_tokens:
            raise ValueError("Vote already submitted")
        if candidate not in election.candidates:
            raise ValueError("Candidate not found")
        election.candidates[candidate] += 1
        election.used_tokens.add(token)
        event = self.audit.record(election_id, token, candidate)
        return {"message": "Vote accepted", "receipt": event["voter_hash"]}
    
    def results(self, election_id):
        election = self.elections.get(election_id)
        return {
            "title": election.title,
            "votes": election.candidates,
            "total_votes": sum(election.candidates.values())
        }
        
# Done