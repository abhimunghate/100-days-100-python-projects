# This is Day 96 project : Online Voting System

import json
from audit import AuditLog
from elections import ElectionService
from voting import VotingService

def show(action, data, status=200):
    print(f"\nREQUEST {action}\nRESPONSE {status}\n{json.dumps(data, indent=2)}")
    
def main():
    print("Day 96 - Online Voting System")
    elections = ElectionService()
    audit = AuditLog()
    voting = VotingService(elections, audit)
    show("POST /api/votes", voting.cast(101, "TOKEN-A1", "Ava Patel"), 201)
    show("POST /api/votes", voting.cast(101, "TOKEN-B2", "Noah Smith"), 201)
    show("GET /api/elections/101/results", voting.results(101))
    show("GET /api/audit", {"events": audit.events})
    
if __name__ == "__main__":
    main()
    
# Done