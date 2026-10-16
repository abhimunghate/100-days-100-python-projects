class Kitchen:
    transitions = {
        "created": "submitted",
        "submitted": "preparing",
        "preparing": "ready",
        "ready": "served"
    }
    
    @classmethod
    def advance(cls, order):
        next_status = cls.transitions.get(order.status)
        if not next_status:
            raise ValueError("Order is already complete")
        order.status = next_status
        return {"order_id": order.id, "status": order.status}
    
# Done