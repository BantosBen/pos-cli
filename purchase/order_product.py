import calendar
import time


class OrderProduct:
    def __init__(self, _name, _amount, _product_id, _quantity):
        """Creates an object of the order product item"""
        self.name = _name
        self.amount = _amount
        self.product_id = _product_id
        self.quantity = _quantity

    def to_dict(self):
        """Returns the equivalent version of the dictionary """
        return {
            "product_id": self.product_id,
            "name": self.name,
            "amount": self.amount,
            "quantity": self.quantity
        }
