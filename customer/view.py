def display_customer_sub_menu():
    """Displays the main customer menu"""
    print("\n--------------------------\n\tCUSTOMER MENU\n--------------------------")
    print(
        "1) Add Customer\n2) Update Customer\n3) Delete Customer\n4) Display all customers\n5) Search customers\n0) "
        "Home")
    return input("pos-cli\\customer$ ")


def add_customer_view():
    """Displays the form to collect new customer's data"""
    name = str(input("Enter Customer Name: "))
    national_id = str(input("Enter Customer National Id: "))
    phone = str(input("Enter Customer Phone: "))
    email = str(input("Enter Customer Email: "))

    confirm = str(input("\nDo you wish to submit this form (y/n): ")).lower()
    if confirm == "y":
        return name, national_id, phone, email
    else:
        return None, None, None, None


def update_customer_view():
    """Displays the customer update sub menu"""
    customer_id = str(input("Enter Customer ID: "))
    field = int(
        input("Which field do you wish to update:\n\t1) Name\n\t2) Email\n\t3) Phone\n\t4) National ID\n\t>> "))
    new_value = str(input("Enter the new value: "))

    confirm = str(input("\nDo you wish to submit this form (y/n): ")).lower()
    if confirm == "y":
        return customer_id, field, new_value
    else:
        return None, None, None


def search_customer_view():
    """Displays the customer search sub menu"""
    field = int(
        input("Select search field:\n\t1) Name\n\t2) Email\n\t3) Phone\n\t4) National ID\n\t>> "))
    keyword = str(input("Enter the search keyword: "))

    confirm = str(input("\nDo you wish to submit this form (y/n): ")).lower()
    if confirm == "y":
        return field, keyword
    else:
        return None, None


def delete_customer_view():
    """Displays the customer delete form"""
    customer_id = str(input("Enter Customer ID: "))

    confirm = str(input("\nDo you wish to submit this form (y/n): ")).lower()
    if confirm == "y":
        return customer_id
    else:
        return None
