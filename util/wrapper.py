from texttable import Texttable
from . import colors as col
import re


def isValidEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def isValidPhone(phone):
    if re.findall(r"^(07|01)([0-9|7])(\d){7}", phone):
        return True
    else:
        return False


def printDataTable(table_data):
    table = Texttable()
    table.set_cols_dtype(["t" for _ in range(len(table_data[0]))])
    table.add_rows(table_data)
    print(table.draw())


def print_error_message(_message):
    print(
        col.Colors.FAIL + _message + col.Colors.END_C)


def print_success_message(_message):
    print(
        col.Colors.OK_GREEN + _message + col.Colors.END_C)


def print_title(_message):
    print(col.Colors.BOLD + _message + col.Colors.END_C)
