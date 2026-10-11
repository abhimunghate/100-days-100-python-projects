# This is Day 92 project : Online Quiz App

import json
from questions import QuestionBank
from quiz import QuizSession

def show(action, data, status=200):
    print(f"\nREQUEST {action}\nRESPONSE {status}\n{json.dumps(data, indent=2)}")
    
def main():
    print("Day 92 - Online Quiz App")
    bank = QuestionBank()
    session = QuizSession(bank.all(), "Arjun")
    show(
        "GET /api/questions",
        {
            "questions": [
                {"id": q.id, "prompt": q.prompt, "options": q.options}
                for q in bank.all()
            ]
        }
    )
    for qid, answer in [(1, "def"), (2, "set"), (3, "3")]:
        show("POST /api/answers", session.submit(qid, answer), 201)
    show("GET /api/results", session.results())
    
if __name__ == "__main__":
    main()
    
# Done