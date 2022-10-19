import re


def isValidPhone(phone):
    if re.findall(r"^(07|01)([0-9|7])(\d){7}", phone):
        return True
    else:
        return False


while True:
    phone = input("Enter Phone: ")
    print(isValidPhone(phone))
