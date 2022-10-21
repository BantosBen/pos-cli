import calendar
import time


class Order:
    def __init__(self, _customer_id, _amount, _items):
        """Creates the order object"""
        self.customer_id = _customer_id
        self.amount = _amount
        self.items = _items
        self.__generate_data()

    def __generate_data(self):
        """Generates the order ID and gets the current date"""
        self.order_id = str(calendar.timegm(time.gmtime()))
        self.order_date = time.strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        """Returns the dictionary version of the order object data"""
        return {
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "amount": self.amount,
            "order_date": self.order_date,
            "items": self.items
        }
