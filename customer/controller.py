from util import file_util as util
from . import view
from . import customer
import util.wrapper as wrapper


class CustomerController:
    def __init__(self):
        self.file_util = util.FileUtil(_table_name="customer")
        self.data = self.file_util.read_data()
        self.fields = ["name", "email", "phone", "national_id", "customer_id"]
        self.table_headers = ["Customer ID", "Name", "National ID", "Phone", "Email"]

    def displayMenu(self):
        while True:
            user_choice = view.display_customer_sub_menu()
            if user_choice == "1":
                _name, _national_id, _phone, _email = view.add_customer_view()
                if _name is not None:
                    if wrapper.isValidEmail(_email):
                        if wrapper.isValidPhone(_phone):
                            self.save_new_customer(customer.Customer(_name, _national_id, _phone, _email))
                        else:
                            wrapper.print_error_message('\nRegistration Failed! Invalid Phone Number')
                    else:
                        wrapper.print_error_message('\nRegistration Failed! Invalid Email')
                else:
                    wrapper.print_error_message('\nSubmission aborted!')
            elif user_choice == "2":
                customer_id, field, new_value = view.update_customer_view()
                if 0 < field <= 4:
                    if customer_id is not None:
                        self.update_customer(customer_id, self.fields[field - 1], new_value)
                    else:
                        wrapper.print_error_message('\nSubmission aborted!')
                else:
                    wrapper.print_error_message("\nFailed to process your request. Invalid field.")

            elif user_choice == "3":
                customer_id = view.delete_customer_view()
                if customer_id is not None:
                    self.delete_customer(customer_id)
            elif user_choice == "4":
                self.display_all_customers()
            elif user_choice == "5":
                field, keyword = view.search_customer_view()
                if 0 < field <= 4:
                    if field is not None:
                        self.search_customer(self.fields[field - 1], keyword)
                    else:
                        wrapper.print_error_message('\nSubmission aborted!')
                else:
                    wrapper.print_error_message("\nFailed to process your request. Invalid field.")
            elif user_choice == "0":
                break
            else:
                wrapper.print_error_message('\nFailed to process your request. Invalid choice.')

    def save_new_customer(self, model):
        self.data.append(model.to_dict())
        self.file_util.write_data(self.data)
        wrapper.print_success_message("\nSaved successfully")

    def customer_exists(self, _customer_id):
        for record in self.data:
            if record["customer_id"] == _customer_id:
                return True
        return False

    def update_customer(self, customer_id, field, new_value):
        for i in range(len(self.data)):
            if self.data[i]["customer_id"] == customer_id:
                self.data[i][field] = new_value
                self.file_util.write_data(self.data)
                wrapper.print_success_message("\nUpdate successful!")
                return
        wrapper.print_error_message("\nUpdate failed. Customer ID not found")

    def display_all_customers(self):
        table_data = list()
        for i in range(len(self.data)):
            table_data.append(self.data[i])
        wrapper.print_title("\nAll customers")
        if len(table_data) > 0:
            self.__prepare_table_data(table_data)
        else:
            wrapper.print_title("\n\tNo customer records yet")

    def search_customer(self, field, keyword):
        table_data = list()
        for i in range(len(self.data)):
            if keyword.lower() in str(self.data[i][field]).lower():
                table_data.append(self.data[i])
        wrapper.print_title("\nSearch result for {}:'{}'".format(field, keyword))
        if len(table_data) > 0:
            self.__prepare_table_data(table_data)
        else:
            wrapper.print_title("\n\tNo customer found")

    def delete_customer(self, customer_id):
        for i in range(len(self.data)):
            if self.data[i]["customer_id"] == customer_id:
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
