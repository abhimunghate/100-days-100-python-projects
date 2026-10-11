from dataclasses import dataclass

@dataclass
class Question:
    id: int
    prompt: str
    options: list[str]
    correct_answer: str
    explanation: str
    
class QuestionBank:
    def __init__(self):
        self.questions = [
            Question(
                1,
                "Which keyword defines a Python function?",
                ["class", "def", "func", "return"],
                "def",
                "Python uses def to begin a function definition."
            ),
            Question(
                2,
                "Which collection stores unique values?",
                ["list", "tuple", "set", "string"],
                "set",
                "A set keeps only unique values."
            ),
            Question(
                3,
                "What does len([10, 20, 30]) return?",
                ["2", "3", "30", "Error"],
                "3",
                "len returns the number of items."
            )
        ]
        
    def all(self):
        return list(self.questions)
    
# Done