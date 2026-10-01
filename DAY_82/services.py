from datetime import date, timedelta
from uuid import uuid4

from models import Loan

class LibraryError(Exception):
    def __init__(self, status, message):
        self.status = status
        self.message = message
        super().__init__(message)
        
class LibraryService:
    def __init__(self, repository):
        self.repository = repository
        
    def list_books(self):
        return {"books": [book.to_dict() for book in self.repository.list_books()]}
    
    def borrow_book(self, member_id, book_id):
        member = self.repository.get_member(member_id)
        book = self.repository.get_book(book_id)
        
        if not member:
            raise LibraryError(404, "Member not found")
        if not book:
            raise LibraryError(404, "Book not found")
        if book.available_copies < 1:
            raise LibraryError(409, "Book is currently unavailable")
        
        today = date.today()
        loan = Loan(
            id=f"LOAN-{uuid4().hex[:8].upper()}",
            book_id=book.id,
            member_id=member.id,
            borrowed_on=today,
            due_on=today + timedelta(days=14)
        )
        book.available_copies -= 1
        self.repository.save_loan(loan)
        
        return {
            "message": "Book borrowed successfully",
            "book": book.title,
            "member": member.name,
            "loan": loan.to_dict()
        }
        
    def return_book(self, loan_id):
        loan = self.repository.get_loan(loan_id)
        if not loan:
            raise LibraryError(404, "Loan not found")
        if loan.returned_on:
            raise LibraryError(409, "Book has already been returned")
        
        loan.returned_on = date.today()
        book = self.repository.get_book(loan.book_id)
        book.available_copies += 1
        
        return {
            "message": "Book returned successfully",
            "book": book.title,
            "loan": loan.to_dict()
        }
        
# Done