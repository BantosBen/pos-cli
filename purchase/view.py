from tabulate import tabulate


def display_product_sub_menu():
    print("\n--------------------------\n\tPURCHASE MENU\n--------------------------")
    print(
        "1) Make new purchase\n2) View customer purchase history\n3) View order details\n0) Home")
    return input("pos-cli\\purchase$ ")


def customer_authentication_view():
    return str(input("Enter customer ID: "))


def product_details_view():
    product_id = str(input("Enter product ID: "))
    quantity = str(input("Enter product quantity: "))
    return product_id, quantity


def confirmation_view(_message="\nDo you wish to continue shopping (y/n): "):
    return str(input(_message)).lower()


def ask_order_id_view():
    return str(input("Enter order ID: "))


def print_receipt(order_info):
    print("\n\t\tPOS-CLI RECEIPT")
    print("Order ID:", order_info.order_id)
    print("Date:", order_info.order_date)

    receipt_header = ['Items', 'Qty', 'Total']
    receipt_content = list()
    items = order_info.items
    for item in items:
        receipt_content.append([item['name'], item['quantity'], item['amount']])

    print(tabulate(receipt_content, headers=receipt_header))
    print('\n')
