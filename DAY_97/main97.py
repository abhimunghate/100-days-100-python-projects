# This is Day 97 project : Restaurant Ordering System

import json
from kitchen import Kitchen
from menu import Menu
from orders import OrderService

def order_data(order):
    return {
        "order_id": order.id,
        "table": order.table,
        "items": order.items,
        "total": order.total,
        "status": order.status
    }
    
def show(action, data, status=200):
    print(f"\nREQUEST {action}\nRESPONSE {status}\n{json.dumps(data, indent=2)}")
    
def main():
    print("Day 97 - Restaurant Ordering System")
    menu = Menu()
    orders = OrderService(menu)
    show("GET /api/menu", {"items": [i.to_dict() for i in menu.list()]})
    order = orders.create(12)
    orders.add_item(order.id, 1, 2)
    orders.add_item(order.id, 3, 1)
    show("POST /api/orders", order_data(order), 201)
    for _ in range(4):
        show("PATCH /api/kitchen/status", Kitchen.advance(order))
        
if __name__ == "__main__":
    main()
    
# Done