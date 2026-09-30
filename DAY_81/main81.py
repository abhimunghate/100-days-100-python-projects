# This is Day 81 project : E-Commerce Backend System

import json
from datetime import datetime, timezone
from uuid import uuid4
from repository import StoreRepository
from services import StoreError, StoreService

class StoreAPI:
    """Routes CLI requests as a small web API would."""
    def __init__(self):
        self.service = StoreService(StoreRepository())
        
    def handle(self, method, path, body=None):
        request_id = f"REQ-{uuid4().hex[:8].upper()}"
        
        try:
            if method == "GET" and path == "/api/products":
                return self._response(200, self.service.list_products(), request_id)
            
            if method == "POST" and path == "/api/carts":
                return self._response(201, self.service.create_cart(), request_id)
            
            if method == "POST" and path.startswith("/api/carts/") and path.endswith("/items"):
                cart_id = path.split("/")[3]
                data = self.service.add_item(
                    cart_id,
                    int(body.get("product_id", 0)),
                    int(body.get("quantity", 0))
                )
                return self._response(200, data, request_id)
            
            if method == "POST" and path.startswith("/api/orders/checkout/"):
                cart_id = path.rsplit("/", 1)[-1]
                return self._response(201, self.service.checkout(cart_id), request_id)
            
            return self._response(404, {"error": "Endpoint not found"}, request_id)
        except StoreError as error:
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
    print("E-Commerce Backend System - CLI Simulation")
    api = StoreAPI()
    
    send(api, "GET", "/api/products")
    
    cart_response = send(api, "POST", "/api/carts")
    cart_id = cart_response["data"]["cart_id"]
    
    send(api, "POST", f"/api/carts/{cart_id}/items", {
        "product_id": 102,
        "quantity": 2
    })
    
    send(api, "POST", f"/api/orders/checkout/{cart_id}")
    
if __name__ == "__main__":
    main()
    
# Done