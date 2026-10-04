# This is Day 85 project : Job Board App

import json
from applications import ApplicationService
from jobs import JobCatalog

def show(action, result, status=200):
    print(f"\nREQUEST {action}\nRESPONSE {status}\n{json.dumps(result, indent=2)}")
    
def main():
    print("Day 85 - Job Board App")
    jobs = JobCatalog()
    applications = ApplicationService(jobs)
    
    show("LIST JOBS", {"jobs": [j.to_dict() for j in jobs.list()]})
    show("SUBMIT APPLICATION", applications.submit(101, "Jordan Lee", "jordan@example.com", "https://files.example.com/jordan.pdf"), 201)
    
if __name__ == "__main__":
    main()
    
# Done