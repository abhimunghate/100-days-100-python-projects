from dataclasses import asdict, dataclass

@dataclass
class MenuItem:
    id: int
    name: str
    category: str
    price: float
    available: bool = True
    
    def to_dict(self):
        return asdict(self)
    
class Menu:
    def __init__(self):
        self.items = {
            1: MenuItem(1, "Margherita Pizza", "Main", 14.5),
            2: MenuItem(2, "Caesar Salad", "Starter", 8.0),
            3: MenuItem(3, "Chocolate Cake", "Dessert", 6.5)
        }
        
    def get(self, item_id):
        item = self.items.get(item_id)
        if not item or not item.available:
            raise LookupError("Menu item unavailable")
        return item
    
    def list(self):
        return list(self.items.values())
    
# Done