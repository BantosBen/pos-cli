from texttable import Texttable
import colors as col


def printDataTable(table_data):
    table = Texttable()
    table.set_cols_dtype(["t" for _ in range(len(table_data[0][0]) + 1)])
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
