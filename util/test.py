import re
from decouple import config


def getPassword():
    print(config('PASSWORD'))


def isValidPhone(phone):
    if re.findall(r"^(07|01)([0-9|7])(\d){7}", phone):
        return True
    else:
        return False


getPassword()
