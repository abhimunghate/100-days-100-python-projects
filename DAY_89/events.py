from dataclasses import dataclass, field

@dataclass
class Event:
    id: int
    name: str
    venue: str
    capacity: int
    bookings: list = field(default_factory=list)
    
    @property
    def available_seats(self):
        return self.capacity - sum(b["seats"] for b in self.bookings if b["status"] == "confirmed")
    
class EventCatalog:
    def __init__(self):
        self.events = {101: Event(101, "Python Developer Conference", "Austin Convention Center", 50)}
        
    def get(self, event_id):
        event = self.events.get(event_id)
        if not event:
            raise LookupError("Event not found")
        return event
    
# Done