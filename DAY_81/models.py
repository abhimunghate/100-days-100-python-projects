from dataclasses import asdict, dataclass, field

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int
    
    def to_dict(self):
        return asdict(self)
    
@dataclass
class CartItem:
    product_id: int
    name: str
    price: float
    quantity: int
    
    def to_dict(self):
        data = asdict(self)
        data["line_total"] = round(self.price * self.quantity, 2)
        return data
    
@dataclass
class Cart:
    id: str
    items: list[CartItem] = field(default_factory=list)
    
    @property
    def total(self):
        return round(sum(item.price * item.quantity for item in self.items), 2)
    
    def to_dict(self):
        return {
            "cart_id": self.id,
            "items": [item.to_dict() for item in self.items],
            "total": self.total,
            "currency": "USD"
        }
        
@dataclass
class Order:
    id: str
    cart_id: str
    items: list[CartItem]
    total: float
    status: str = "confirmed"
    
    def to_dict(self):
        return {
            "order_id": self.id,
            "cart_id": self.cart_id,
            "status": self.status,
            "items": [item.to_dict() for item in self.items],
            "total": self.total,
            "currency": "USD"
        }
        
# Done