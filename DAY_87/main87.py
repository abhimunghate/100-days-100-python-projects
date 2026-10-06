# This is Day 87 project : Online Polling System

import json
from polls import PollService
from voting import VotingService

def show(action, result, status=200):
    print(f"\nREQUEST {action}\nRESPONSE {status}\n{json.dumps(result, indent=2)}")
    
def main():
    print("Day 87 - Online Polling System")
    
    polls = PollService()
    voting = VotingService(polls)
    
    poll = polls.get(101)
    show("GET POLL", {"id": poll.id, "question": poll.question, "options": poll.options})
    show("CAST VOTE", voting.vote(101, "USR-501", "API"), 201)
    show("GET RESULTS", {"results": poll.options})
    
if __name__ == "__main__":
    main()
    
# Done