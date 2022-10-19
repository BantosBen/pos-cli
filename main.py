import pyfiglet
from customer import controller as customer_controller
from product import controller as product_controller
from purchase import controller as purchase_controller


def main():
    printTitle()
    while True:
        print("\n--------------------------\n\tMAIN MENU\n--------------------------")
        print("1) Customer\n2) Product\n3) Purchase\n0) Exit")
        user_choice = input("pos-cli$ ")
        if user_choice == "1":
            customer_controller.CustomerController().displayMenu()
        elif user_choice == "2":
            product_controller.ProductController().displayMenu()
        elif user_choice == "3":
            purchase_controller.ProductController().displayMenu()
        elif user_choice == "0":
            print("app shutting down...")
            break
        else:
            print("\tCould not process your request. Invalid choice\n")


def printTitle():
    my_title = pyfiglet.figlet_format("P O S - C L I")
    print(my_title)


def printProductSubMenu():
    print("1) Add Product\n2) Update Product\n3) Delete Product\n4) Display all Product\n0) Home")
    user_choice = input("pos-cli\\product$ ")


def printPurchaseSubMenu():
    print("1) Make new Purchase\n2) Purchase Summary by Customer\n3) Display all Purchase\n0) Home")
    user_choice = input("pos-cli\\purchase ")


if __name__ == '__main__':
    main()
