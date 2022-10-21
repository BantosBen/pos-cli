import calendar
import time


class Customer:
    def __init__(self, _name, _national_id, _phone, _email):
        """Creates the customer objects"""
        self.name = _name
        self.national_id = _national_id
        self.phone = _phone
        self.email = _email
        self.__generate_customer_id()

    def __generate_customer_id(self):
        """Gets the current timestamp and uses it as the customer ID"""
        self.customer_id = str(calendar.timegm(time.gmtime()))

    def to_dict(self):
        """Creates a dictionary version of the object data"""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "national_id": self.national_id,
            "phone": self.phone,
            "email": self.email
        }
