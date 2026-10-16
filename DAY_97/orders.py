from dataclasses import dataclass, field

@dataclass
class Order:
    id: str
    table: int
    items: list = field(default_factory=list)
    status: str = "created"
    
    @property
    def total(self):
        return round(sum(i["price"] * i["quantity"] for i in self.items), 2)
    
class OrderService:
    def __init__(self, menu):
        self.menu, self.orders = menu, {}
        
    def create(self, table):
        order = Order(f"ORD-{len(self.orders)+1:04}", table)
        self.orders[order.id] = order
        return order
    
    def add_item(self, order_id, item_id, quantity):
        order = self.orders.get(order_id)
        if not order:
            raise LookupError("Order not found")
        if quantity < 1:
            raise ValueError("Quantity must be positive")
        item = self.menu.get(item_id)
        order.items.append(
            {
                "item_id": item.id,
                "name": item.name,
                "price": item.price,
                "quantity": quantity
            }
        )
        return order
    
# Done