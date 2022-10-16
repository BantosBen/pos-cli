def display_product_sub_menu():
    print("\n--------------------------\n\tPRODUCT MENU\n--------------------------")
    print(
        "1) Add Product\n2) Update Product\n3) Delete Product\n4) Display all products\n5) Search products\n0) "
        "Home")
    return input("pos-cli\\product$ ")


def add_product_view():
    name = str(input("Enter product name: "))
    price = str(input("Enter product price : "))
    quantity = str(input("Enter product quantity: "))

    confirm = str(input("\nDo you wish to submit this form (y/n): ")).lower()
    if confirm == "y":
        return name, price, quantity
    else:
        return None, None, None, None


def update_product_view():
    product_id = str(input("Enter Product ID: "))
    field = int(
        input("Which field do you wish to update:\n\t1) Name\n\t2) Price\n\t3) Quantity"))
    new_value = str(input("Enter the new value: "))

    confirm = str(input("\nDo you wish to submit this form (y/n): ")).lower()
    if confirm == "y":
        return product_id, field, new_value
    else:
        return None, None, None


def search_product_view():
    field = int(
        input("Select search field:\n\t1) Name\n\t2) Product ID"))
    keyword = str(input("Enter the search keyword: "))

    confirm = str(input("\nDo you wish to submit this form (y/n): ")).lower()
    if confirm == "y":
        return field, keyword
    else:
        return None, None


def delete_product_view():
    product_id = str(input("Enter Product ID: "))

    confirm = str(input("\nDo you wish to submit this form (y/n): ")).lower()
    if confirm == "y":
        return product_id
    else:
        return None
