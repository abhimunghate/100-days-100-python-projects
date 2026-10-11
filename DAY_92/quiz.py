class QuizSession:
    def __init__(self, questions, participant):
        self.questions, self.participant, self.answers = questions, participant, {}
        
    def submit(self, question_id, answer):
        question = next((q for q in self.questions if q.id == question_id), None)
        if not question:
            raise LookupError("Question not found")
        if answer not in question.options:
            raise ValueError("Answer must match one of the options")
        self.answers[question_id] = answer
        return {"question_id": question_id, "accepted": True}
    
    def results(self):
        details = []
        for q in self.questions:
            answer = self.answers.get(q.id)
            correct = answer == q.correct_answer
            details.append(
                {
                    "question_id": q.id,
                    "answer": answer,
                    "correct": correct,
                    "correct_answer": q.correct_answer,
                    "explanation": q.explanation
                }
            )
        score = sum(1 for item in details if item["correct"])
        return {
            "participant": self.participant,
            "score": score,
            "total": len(self.questions),
            "percentage": round(score / len(self.questions) * 100, 1),
            "details": details
        }
        
# Done