# This is Day 89 project : Event Booking App

import json
from bookings import BookingService
from events import EventCatalog

def show(action, result, status=200):
    print(f"\nREQUEST {action}\nRESPONSE {status}\n{json.dumps(result, indent=2)}")
    
def main():
    print("Day 89 - Event Booking App")
    events = EventCatalog()
    bookings = BookingService(events)
    event = events.get(101)
    
    show("GET EVENT", {"id": event.id, "name": event.name, "available_seats": event.available_seats})
    booking = bookings.create(101, "Mia Chen", 3)
    show("CREATE BOOKING", booking, 201)
    show("CANCEL BOOKING", bookings.cancel(101, booking["id"]))
    show("GET AVAILABILITY", {"available_seats": event.available_seats})
    
if __name__ == "__main__":
    main()
    
# Done