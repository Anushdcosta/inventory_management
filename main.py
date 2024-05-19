from function import *
import sys

# Function to create instances of InventoryItem from CSV rows
print("""
Which Section's inventory would you like to access:
    1) Gaming Hardware Section
    2) Food Section
""")
while True:
    try:
        user_opt = int(input("Enter a option from the above list: "))
        if user_opt not in range(0,3):
            raise Exception
        break
    except:
        print("Please Enter a valid option")
if user_opt == 1:
    inventory_items = create_inventory_objects_from_gaming_csv('csv_files/gaming_inventory.csv')
    company = 1
if user_opt == 2:
    inventory_items = create_inventory_objects_from_food_csv('csv_files/foods_inventory.csv')
    company = 2
print("\n")
def exiter():
    val = continuer("continue")
    if val == 0:
        exit()
    else:
        main()
def kill():
    sys.exit()
def main():
    print("""Welcome to the inventory management system:
    1) View the list of items in the inventory. 
    2) View the properties of a specific item.
    3) Update the properties of an item.
    4) Check whether any items in the inventory
    need to be reordered.
    5) Add a new item to the inventory
    6) Update Sold items into inventory
    7) Back to Section Selection
    8) Quit
        """)
    while True:
        try:
            user_opt = int(input("Enter your option from the above list : "))
            break
        except:
            print("Please enter a number between 1 and 8.")

    if user_opt == 8:
        print("THANK YOU FOR USING THIS INVENTORY MANAGER")
        kill()
    else:
        match user_opt:
            case 1:
                item_list_viewer(inventory_items, "view", company)
            case 2:
                properties_viewer(inventory_items, company)
            case 3:
                while True:
                    update_objects(inventory_items, company)
                    redo = continuer(f"edit another item's properties")
                    if redo == 1:
                        print("Alright")
                    else:
                        break
            case 4:
                reorder_checker(inventory_items)
            case 5:
                add_item(inventory_items, company)
            case 6:
                Sold_items(inventory_items, company)
            case 7:
                os.system("py main.py")
            case _:
                print("Please enter a number between 1 and 7.")
        exiter()

main()