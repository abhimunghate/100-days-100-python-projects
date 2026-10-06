class VotingService:
    def __init__(self, polls):
        self.polls = polls
        
    def vote(self, poll_id, voter_id, option):
        poll = self.polls.get(poll_id)
        
        if voter_id in poll.voters:
            raise ValueError("Voter has already voted")
        
        if option not in poll.options:
            raise ValueError("Invalid option")
        
        poll.options[option] += 1
        poll.voters.add(voter_id)
        
        return {"message": "Vote recorded", "results": poll.options, "total_votes": sum(poll.options.values())}
    
# Done