from models import Book, Member

class LibraryRepository:
    """In-memory storage used in place of a database."""
    
    def __init__(self):
        self.books = {
            101: Book(101, "Clean Code", "Robert C. Martin", 2),
            102: Book(102, "The Pragmatic Programmer", "David Thomas", 1),
            103: Book(103, "Python Crash Course", "Eric Matthes", 3)
        }
        self.members = {
            501: Member(501, "Ava Patel", "ava@example.com"),
            502: Member(502, "Noah Smith", "noah@example.com")
        }
        self.loans = {}
        
    def list_books(self):
        return list(self.books.values())
    
    def get_book(self, book_id):
        return self.books.get(book_id)
    
    def get_member(self, member_id):
        return self.members.get(member_id)
    
    def save_loan(self, loan):
        self.loans[loan.id] = loan
        
    def get_loan(self, loan_id):
        return self.loans.get(loan_id)
    
# Done