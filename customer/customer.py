import calendar
import time


class Customer:
    def __init__(self, _name, _national_id, _phone, _email):
        self.name = _name
        self.national_id = _national_id
        self.phone = _phone
        self.email = _email
        self.__generate_customer_id()

    def __generate_customer_id(self):
        self.customer_id = calendar.timegm(time.gmtime())

    def to_dict(self):
        return {
            "name": self.name,
            "national_id": self.national_id,
            "phone": self.phone,
            "email": self.email,
            "customer_id": self.customer_id
        }
