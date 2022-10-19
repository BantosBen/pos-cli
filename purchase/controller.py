from util import file_util as util
from customer import controller as cc
from product import controller as pc
from . import view
from . import order_product as op
from . import order as order
import util.wrapper as wrapper


class ProductController:
    def __init__(self):
        self.customer_id = None
        self.file_util = util.FileUtil(_table_name="order")
        self.data = self.file_util.read_data()
        self.table_headers = ["Product ID", "Name", "Price", "Quantity"]
        self.customer = cc.CustomerController()
        self.product = pc.ProductController()
        self.order_products = list()

    def displayMenu(self):
        while True:
            user_choice = view.display_product_sub_menu()
            if user_choice == "1":
                self.customer_id = view.customer_authentication_view()
                if self.customer.customer_exists(self.customer_id):
                    self.order_products = list()
                    wrapper.print_success_message("Authentication Successful")
                    raw_order_products = dict()
                    while True:
                        product_id, quantity = view.product_details_view()
                        _, _, db_quantity = self.product.product_info(product_id)
                        if db_quantity is not None:
                            if int(db_quantity) >= int(quantity):
                                if int(quantity) > 0:
                                    if product_id not in raw_order_products:
                                        raw_order_products[product_id] = quantity
                                    else:
                                        raw_order_products[product_id] = int(raw_order_products[product_id]) + int(
                                            quantity)
                                    wrapper.print_success_message("Added to cart successfully")
                                else:
                                    wrapper.print_error_message("Failed to add to cart. Invalid quantity")
                            else:
                                wrapper.print_error_message(
                                    "Failed to add to cart. There are only {} items left".format(db_quantity))
                        else:
                            wrapper.print_error_message("Failed to add to cart. No such product ID found")

                        user_confirmation = view.confirmation_view()

                        if user_confirmation != 'y':
                            self.prepare_order(raw_order_products)
                            break

                else:
                    wrapper.print_error_message("Authentication failed. No such customer ID found")

            elif user_choice == "2":
                self.customer_id = view.customer_authentication_view()
                if self.customer_id is not None:
                    self.prepare_customer_order_history()
                else:
                    wrapper.print_error_message("\nFailed to process your request. Invalid customer ID.")

            elif user_choice == "3":
                order_id = view.ask_order_id_view()
                if order_id is not None:
                    self.prepare_order_details(order_id)
                else:
                    wrapper.print_error_message("\nFailed to process your request. Invalid customer ID.")
            elif user_choice == "0":
                break
            else:
                wrapper.print_error_message('\nFailed to process your request. Invalid choice.')

    def __save_new_product(self, model):
        self.data.append(model.to_dict())
        self.file_util.write_data(self.data)
        wrapper.print_success_message("\nSaved successfully")

    def check_id(self, _product_id):
        for record in self.data:
            if record["product_id"] == _product_id:
                return True
        return False

    def __update_product(self, product_id, field, new_value):
        for i in range(len(self.data)):
            if self.data[i]["product_id"] == product_id:
                self.data[i][field] = new_value
                self.file_util.write_data(self.data)
                wrapper.print_success_message("\nUpdate successful!")
                return
        wrapper.print_error_message("\nUpdate failed. Product ID not found")

    def __delete_product(self, product_id):
        for i in range(len(self.data)):
            if self.data[i]["product_id"] == product_id:
                self.data.pop(i)
                self.file_util.write_data(self.data)
                wrapper.print_success_message("\nDelete successful!")
                return
        wrapper.print_error_message("\nDelete failed. Customer ID not found")

    def prepare_order(self, raw_order_products):
        for product_id, quantity in raw_order_products.items():
            price, name, _ = self.product.product_info(product_id)
            amount = float(price) * int(quantity)
            self.order_products.append(op.OrderProduct(name, amount, product_id, quantity))
        wrapper.print_success_message("Order prepared successfully")
        user_confirmation = view.confirmation_view("\nDo you wish to place this order (y/n): ")

        if user_confirmation == 'y':
            self.product.updateQuantity(raw_order_products)
            self.place_order()

    def place_order(self):
        items = list()
        order_amount = 0
        for order_product in self.order_products:
            items.append(order_product.to_dict())
            order_amount += order_product.amount

        order_info = order.Order(self.customer_id, order_amount, items)
        self.data.append(order_info.to_dict())
        self.file_util.write_data(self.data)
        wrapper.print_success_message("\nOrder placed successfully")
        view.print_receipt(order_info)

    def prepare_customer_order_history(self):
        table_data = list()
        table_data.append(['Order ID', 'Amount', 'Date'])
        for order_info in self.data:
            if order_info['customer_id'] == self.customer_id:
                table_data.append([order_info['order_id'], order_info['amount'], order_info['order_date']])

        if len(table_data) > 1:
            wrapper.print_title("\n\tCustomer Order History")
            wrapper.printDataTable(table_data)
        else:
            wrapper.print_title("\n\t\tNo orders found for the customer ID")

    def prepare_order_details(self, order_id):
        table_data = list()
        table_data.append(['Items', 'Qty', 'Total'])
        for order_info in self.data:
            if order_info['order_id'] == order_id:
                wrapper.print_title("\n\tOrder Details")
                print("Order ID:", order_info['order_id'], end='\t')
                print("Customer ID:", order_info['customer_id'])
                print("Order Date:", order_info['order_date'], end='\t')
                print("Total Amount:", order_info['amount'])
                items = order_info['items']
                for item in items:
                    table_data.append([item['name'], item['quantity'], item['amount']])
                break

        if len(table_data) > 1:
            wrapper.printDataTable(table_data)
        else:
            wrapper.print_title("\n\t\tNo orders found for the customer ID")
