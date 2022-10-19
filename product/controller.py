from util import file_util as util
from . import view
from . import product
import util.wrapper as wrapper


class ProductController:
    def __init__(self):
        self.file_util = util.FileUtil(_table_name="product")
        self.data = self.file_util.read_data()
        self.table_headers = ["Product ID", "Name", "Price", "Quantity"]

    def displayMenu(self):
        while True:
            user_choice = view.display_product_sub_menu()
            if user_choice == "1":
                name, price, quantity = view.add_product_view()
                if name is not None:
                    self.__save_new_product(product.Product(name, price, quantity))
                else:
                    wrapper.print_error_message('\nSubmission aborted!')

            elif user_choice == "2":
                fields = ["name", "price", "quantity"]
                product_id, field, new_value = view.update_product_view()
                if 0 < field <= 3:
                    if product_id is not None:
                        if self.__update_product(product_id, fields[field - 1], new_value):
                            wrapper.print_success_message("\nUpdate successful!")
                    else:
                        wrapper.print_error_message('\nSubmission aborted!')
                else:
                    wrapper.print_error_message("\nFailed to process your request. Invalid field.")

            elif user_choice == "3":
                product_id = view.delete_product_view()
                if product_id is not None:
                    self.__delete_product(product_id)
            elif user_choice == "4":
                self.__display_all_products()
            elif user_choice == "5":
                fields = ["name", "product_id"]
                field, keyword = view.search_product_view()
                if 0 < field <= 2:
                    if field is not None:
                        self.__search_product(fields[field - 1], keyword)
                    else:
                        wrapper.print_error_message('\nSubmission aborted!')
                else:
                    wrapper.print_error_message("\nFailed to process your request. Invalid field.")
            elif user_choice == "0":
                break
            else:
                wrapper.print_error_message('\nFailed to process your request. Invalid choice.')

    def __save_new_product(self, model):
        self.data.append(model.to_dict())
        self.file_util.write_data(self.data)
        wrapper.print_success_message("\nSaved successfully")

    def product_info(self, _product_id):
        for record in self.data:
            if record["product_id"] == _product_id:
                return record['price'], record['name'], record['quantity']
        return None, None, None

    def product_exists(self, _product_id):
        for record in self.data:
            if record["product_id"] == _product_id:
                return True
        return False

    def __update_product(self, product_id, field, new_value):
        for i in range(len(self.data)):
            if self.data[i]["product_id"] == product_id:
                self.data[i][field] = new_value
                self.file_util.write_data(self.data)
                return True
        wrapper.print_error_message("\nUpdate failed. Product ID not found")
        return False

    def __display_all_products(self):
        table_data = list()
        for i in range(len(self.data)):
            table_data.append(self.data[i])

        wrapper.print_title("\nAll products")
        self.__prepare_table_data(table_data)

    def __search_product(self, field, keyword):
        table_data = list()
        for i in range(len(self.data)):
            if keyword.lower() in str(self.data[i][field]).lower():
                table_data.append(self.data[i])
        wrapper.print_title("\nSearch result for {}:'{}'".format(field, keyword))
        self.__prepare_table_data(table_data)

    def __delete_product(self, product_id):
        for i in range(len(self.data)):
            if self.data[i]["product_id"] == product_id:
                self.data.pop(i)
                self.file_util.write_data(self.data)
                wrapper.print_success_message("\nDelete successful!")
                return
        wrapper.print_error_message("\nDelete failed. Customer ID not found")

    def __prepare_table_data(self, _raw_data):
        table_data = list()
        table_data.append(self.table_headers)
        for datum in _raw_data:
            table_data.append(list(datum.values()))
        wrapper.printDataTable(table_data)

    def updateQuantity(self, raw_order_products):
        for product_id, quantity in raw_order_products.items():
            _, _, db_quantity = self.product_info(product_id)
            new_quantity = int(db_quantity) - int(quantity)
            self.__update_product(product_id, 'quantity', new_quantity)
