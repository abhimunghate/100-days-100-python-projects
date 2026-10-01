# This is Day 82 project : Library Management System

import json
from datetime import datetime, timezone
from uuid import uuid4

from repository import LibraryRepository
from services import LibraryError, LibraryService

class LibraryAPI:
    def __init__(self):
        self.service = LibraryService(LibraryRepository())
        
    def handle(self, method, path, body=None):
        request_id = f"REQ-{uuid4().hex[:8].upper()}"
        
        try:
            if method == "GET" and path == "/api/books":
                return self._response(200, self.service.list_books(), request_id)
            
            if method == "POST" and path == "/api/loans":
                data = self.service.borrow_book(
                    int(body.get("member_id", 0)),
                    int(body.get("book_id", 0))
                )
                return self._response(201, data, request_id)
            
            if method == "POST" and path.startswith("/api/loans") and path.endswith("/return"):
                loan_id = path.split("/")[3]
                return self._response(200, self.service.return_book(loan_id), request_id)
            
            return self._response(404, {"error": "Endpoint not found"}, request_id)
        except LibraryError as error:
            return self._response(error.status, {"error": error.message}, request_id)
        except (TypeError, ValueError):
            return self._response(400, {"error": "Invalid request data"}, request_id)
        
    @staticmethod
    def _response(status, data, request_id):
        return {
            "status": status,
            "request_id": request_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "data": data
        }
        
def send(api, method, path, body=None):
    print(f"\nREQUEST {method} {path}")
    if body:
        print(json.dumps(body, indent=2))
        
    result = api.handle(method, path, body or {})
    print(f"RESPONSE {result['status']}")
    print(json.dumps(result, indent=2))
    return result

def main():
    print("Day 82 - Library Management System")
    api = LibraryAPI()
    
    send(api, "GET", "/api/books")
    
    borrow_response = send(api, "POST", "/api/loans", {
        "member_id": 501,
        "book_id": 102
    })
    loan_id = borrow_response["data"]["loan"]["loan_id"]
    
    send(api, "POST", f"/api/loans/{loan_id}/return")
    send(api, "GET", "/api/books")
    
if __name__ == "__main__":
    main()
    
# Done