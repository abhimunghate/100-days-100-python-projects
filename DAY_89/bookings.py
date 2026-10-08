class BookingService:
    def __init__(self, events):
        self.events = events
        
    def create(self, event_id, customer, seats):
        event = self.events.get(event_id)
        if seats < 1:
            raise ValueError("At least one seat is required")
        if seats > event.available_seats:
            raise ValueError("Not enough seats available")
        
        booking = {"id": f"BOOK-{len(event.bookings)+1:04}", "customer": customer, "seats": seats, "status": "confirmed"}
        event.bookings.append(booking)
        return booking
    
    def cancel(self, event_id, booking_id):
        event = self.events.get(event_id)
        booking = next((b for b in event.bookings if b["id"] == booking_id), None)
        if not booking:
            raise LookupError("Booking not found")
        booking["status"] = "cancelled"
        return booking
    
# Done