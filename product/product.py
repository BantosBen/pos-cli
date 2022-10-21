import calendar
import time


class Product:
    def __init__(self, _name, _price, _quantity):
        """Instantiates the product object"""
        self.name = _name
        self.price = _price
        self.quantity = _quantity
        self.__generate_product_id()

    def __generate_product_id(self):
        """Gets the current timestamp and uses it as the product ID"""
        self.product_id = str(calendar.timegm(time.gmtime()))

    def to_dict(self):
        """Creates the dictionary version of the product model data"""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }
