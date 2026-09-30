from uuid import uuid4
from models import Cart, CartItem, Order

class StoreError(Exception):
    def __init__(self, status, message):
        self.status = status
        self.message = message
        super().__init__(message)
        
class StoreService:
    def __init__(self, repository):
        self.repository = repository
        
    def list_products(self):
        return {"products": [product.to_dict() for product in self.repository.list_products()]}
    
    def create_cart(self):
        cart = Cart(id=f"CART-{uuid4().hex[:8].upper()}")
        self.repository.save_cart(cart)
        return cart.to_dict()
    
    def add_item(self, cart_id, product_id, quantity):
        cart = self.repository.get_cart(cart_id)
        if not cart:
            raise StoreError(404, "Cart not found")
        
        product = self.repository.get_product(product_id)
        if not product:
            raise StoreError(404, "Product not found")
        if quantity < 1:
            raise StoreError(400, "Quantity must be at least 1")
        if quantity > product.stock:
            raise StoreError(409, "Insufficient inventory")
        
        existing = next((item for item in cart.items if item.product_id == product_id), None)
        if existing:
            if existing.quantity + quantity > product.stock:
                raise StoreError(409, "Insufficient inventory")
            existing.quantity += quantity
        else:
            cart.items.append(CartItem(product.id, product.name, product.price, quantity))
            
        self.repository.save_cart(cart)
        return cart.to_dict()
    
    def checkout(self, cart_id):
        cart = self.repository.get_cart(cart_id)
        if not cart:
            raise StoreError(404, "Cart not found")
        if not cart.items:
            raise StoreError(400, "Cart is empty")
        
        for item in cart.items:
            product = self.repository.get_product(item.product_id)
            if item.quantity > product.stock:
                raise StoreError(409, f"Insufficient inventory for {product.name}")
            
        for item in cart.items:
            self.repository.get_product(item.product_id).stock -= item.quantity
            
        order = Order(
            id=f"ORD-{uuid4().hex[:8].upper()}",
            cart_id=cart.id,
            items=list(cart.items),
            total=cart.total
        )
        self.repository.save_order(order)
        return order.to_dict()
    
# Done