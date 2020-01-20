# Simple Inventory Management Program - Alpha 2.0
# See Project Documentation/documentation-Alpha2.txt for more information

import functions

functions.display_intro()
item_list = functions.retrieve_inventory()
functions.display_inventory(item_list)

while True:
    functions.display_menu()
    user_option = input("Enter selection: ")
    # Adding a new inventory item
    if user_option == "1":
        print("Option 1 selected")
        functions.add_item(item_list)
        functions.display_inventory(item_list)
        print("Item added...\n")
    # Removing an inventory item
    elif user_option == "2":
        print("Option 2 selected")
        functions.remove_item(item_list)
        functions.display_inventory(item_list)
        print("Item removed...\n")
    # Update stock count for an item
    elif user_option == "3":
        print("Option 3 selected")
        functions.update_stock(item_list)
        functions.display_inventory(item_list)
        print("Stock count updated...\n")
    # Save & exit
    elif user_option.lower() == "q":
        print("\nSaving inventory list...\nExiting program...")
        functions.save_file(item_list)
        break
    else:
        print("\nInvalid option...\n")
