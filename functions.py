import pickle
import classes


def display_intro():
    from datetime import datetime
    current_dt = datetime.today()
    print("\nSimple Inventory Management Program - Alpha 2.0")
    print("Current data and time: " + str(current_dt) + "\n")


def user_login():
    user_pass = {"username": "password123"}
    verified_user = False
    while verified_user is False:
        print("Please verify your identity...")
        login_name = input("Username: ")
        login_pass = input("Password: ")

        if user_pass.get(login_name) == login_pass:
            print("Verified\n")
            verified_user = True
        else:
            print("Invalid login, please try again\n")


def display_menu():
    print("----------Menu----------")
    print("1. Add item\n2. Remove item\n3. Adjust stock quantity\nType 'q' to save & exit...")
    print("------------------------")


def display_inventory(inventory_list):
    print("--------Inventory-------")
    for item in inventory_list:
        print(item)
    print("------------------------\n")


def save_file(inv_list):
    with open("inventory_list.pickle", "wb") as inv_out:
        pickle.dump(inv_list, inv_out)


def retrieve_inventory():
    with open("inventory_list.pickle", "rb") as inv_in:
        inv_list = pickle.load(inv_in)
        return inv_list


def add_item(item_list):
    item_name = input("\nEnter item name: ")
    item_id = input("Enter item ID number: ")
    item_qty = int(input("Enter item quantity: "))
    new_item = classes.Item(item_name, item_id, item_qty)
    item_list.append(new_item)
    print("Adding item...")


def remove_item(item_list):
    item_in_list = False

    while not item_in_list:
        item_id = input("Enter item ID number: ")
        for item in item_list:
            if item_id == str(item.id_num):
                item_list.remove(item)
                print("Removing item...\n")
                item_in_list = True
        if not item_in_list:
            print("Item not found...\n")


def update_stock(item_list):
    item_in_list = False

    while not item_in_list:
        item_id = input("Enter item ID number: ")
        for item in item_list:
            if item_id == str(item.id_num):
                valid_entry = False
                while not valid_entry:
                    update = input("Increase(+) or decrease(-) the quantity of " + item.name + "?: ")
                    if update == "+":
                        while True:
                            # TODO: Throw an exception if user enters a non-integer; loop prompt
                            qty = int(input("Enter a quantity: "))
                            if qty >= 0:
                                item.stock += qty
                                print("Updating stock count...")
                                valid_entry = True
                                break
                            else:
                                print("Error: Entry must be positive...")
                    elif update == "-":
                        while True:
                            # TODO: Throw an exception if user enters a non-integer; loop prompt
                            qty = int(input("Enter a quantity: "))
                            if (qty >= 0) and (item.stock > qty):
                                item.stock -= qty
                                print("Updating stock count...")
                                valid_entry = True
                                break
                            elif item.stock == qty:
                                item_list.remove(item)
                                print("Removing item...\n")
                                valid_entry = True
                                break
                            else:
                                print("Error: Entry must be positive and cannot exceed current stock count...\n")
                    else:
                        print("Invalid operation...\n")
            item_in_list = True
        if not item_in_list:
            print("Item not found...\n")
