from models import Cart, Order, Product

class StoreRepository:
    """Small in-memory repository used in place of a database."""
    
    def __init__(self):
        self.products = {
            101: Product(101, "Wireless Mouse", 29.99, 12),
            102: Product(102, "Mechanical Keyboard", 79.99, 7),
            103: Product(103, "USB-C Dock", 119.00, 4)
        }
        self.carts: dict[str, Cart] = {}
        self.orders: dict[str, Order] = {}
        
    def list_products(self):
        return list(self.products.values())
    
    def get_product(self, product_id):
        return self.products.get(product_id)
    
    def save_cart(self, cart):
        self.carts[cart.id] = cart
        
    def get_cart(self, cart_id):
        return self.carts.get(cart_id)
    
    def save_order(self, order):
        self.orders[order.id] = order
        
# Done