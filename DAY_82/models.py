from dataclasses import asdict, dataclass
from datetime import date

@dataclass
class Book:
    id: int
    title: str
    author: str
    available_copies: int
    
    def to_dict(self):
        return asdict(self)
    
@dataclass
class Member:
    id: int
    name: str
    email: str
    
    def to_dict(self):
        return asdict(self)
    
@dataclass
class Loan:
    id: str
    book_id: int
    member_id: int
    borrowed_on: date
    due_on: date
    returned_on: date | None = None
    
    def to_dict(self):
        return {
            "loan_id": self.id,
            "book_id": self.book_id,
            "member_id": self.member_id,
            "borrowed_on": self.borrowed_on.isoformat(),
            "due_on": self.due_on.isoformat(),
            "returned_on": self.returned_on.isoformat() if self.returned_on else None,
            "status": "returned" if self.returned_on else "active"
        }
        
# Done