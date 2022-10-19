import calendar
import time


class OrderProduct:
    def __init__(self, _name, _amount, _product_id, _quantity):
        self.name = _name
        self.amount = _amount
        self.product_id = _product_id
        self.quantity = _quantity

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "amount": self.amount,
            "quantity": self.quantity
        }
