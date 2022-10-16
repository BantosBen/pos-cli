import calendar
import time


class Product:
    def __init__(self, _name, _price, _quantity):
        self.name = _name
        self.price = _price
        self.quantity = _quantity
        self.__generate_product_id()

    def __generate_product_id(self):
        self.product_id = str(calendar.timegm(time.gmtime()))

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }
