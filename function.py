import csv
from logging import exception
from class_of_items import *
from datetime import datetime
import os
from dateutil.relativedelta import relativedelta 
import tabulate
#---------------------------------------- OBJECT for gaming hardware
def create_inventory_objects_from_gaming_csv(csv_file):
    inventory_objects = []
    
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convert string values to appropriate types if needed
            row['Quantity'] = int(row['Quantity'])
            row['ReorderLevel'] = int(row['ReorderLevel'])
            row['ReorderQuantity'] = int(row['ReorderQuantity'])
            row['Category'] = int(row['Category'])
            row['UnitCost'] = float(row['UnitCost'])
            row['TotalValue'] = float(row['TotalValue'])
            row['Specs'] = row['Specs']
            row['DateLastUpdated'] = row['DateLastUpdated']
            row['CriticalLevel'] = int(row['CriticalLevel']) if row['CriticalLevel'] else 0
            row['Earned'] = int(row['Earned'])
            row['Sold_items'] = int(row['Sold_items'])
            # Create an instance of InventoryItem for each row
            item = Gaming_company(**row)
            inventory_objects.append(item)
    return inventory_objects
#---------------------------------------- OBJECT for food
def create_inventory_objects_from_food_csv(csv_file):
    inventory_objects = []
    
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convert string values to appropriate types if needed
            row['Quantity'] = int(row['Quantity'])
            row['ReorderLevel'] = int(row['ReorderLevel'])
            row['ReorderQuantity'] = int(row['ReorderQuantity'])
            row['Category'] = int(row['Category'])
            row['UnitCost'] = float(row['UnitCost'])
            row['TotalValue'] = float(row['TotalValue'])
            row['Production_Date'] = row['Production_Date']
            row['Expiration_Date'] = row['Expiration_Date']
            row['CriticalLevel'] = int(row['CriticalLevel']) if row['CriticalLevel'] else 0
            row['Earned'] = int(eval(row['Earned']))
            row['Sold_items'] = int(row['Sold_items'])
            # Create an instance of InventoryItem for each row
            item = Food_company(**row)
            inventory_objects.append(item)
    return inventory_objects
#---------------------------------------- GENERAL
#------- Function to check if user wants to continue +
def continuer(task):
    
    while True:
        try:
            user_continue = int(input(f"Would you like to {task} (1 for Yes, 0 for No): "))
            if user_continue == 1:
                # os.system('cls')
                return 1
            elif user_continue == 0:
                # os.system('cls')
                
                return 0
            else:
                raise Exception
        except:
            print("Please enter 1 for Yes, 0 for No.")
#------- Function to create a dictionary categorizing all items prresent in the inventory. +
def item_list_viewer_category(inventory_items, company):
    items_list = inventory_items
    if company == 1:
        with open("csv_files/gaming_categories.csv") as file:
            read = list(csv.reader(file))
        read.pop(0)
        categories = {}
        for i in read:
            categories[i[1]] = []
        for i in items_list:
            if i.Category == 1:
                categories[list(categories.keys())[0]].append(i)
            elif i.Category == 2:
                categories[list(categories.keys())[1]].append(i)
            elif i.Category == 3:
                categories[list(categories.keys())[2]].append(i)
            elif i.Category == 4:
                categories[list(categories.keys())[3]].append(i)
            elif i.Category == 5:
                categories[list(categories.keys())[4]].append(i)
            elif i.Category == 6:
                categories[list(categories.keys())[5]].append(i)
            elif i.Category == 7:
                categories[list(categories.keys())[6]].append(i)
            elif i.Category == 8:
                categories[list(categories.keys())[7]].append(i)
            elif i.Category == 9:
                categories[list(categories.keys())[8]].append(i)
            elif i.Category == 10:
                categories[list(categories.keys())[9]].append(i)
            elif i.Category == 11:
                categories[list(categories.keys())[10]].append(i)
        for i in categories:
            print(f"{list(categories.keys()).index(i)+1})",i.upper())
         
        return categories
    if company == 2:
        categories = {"Fruits":[], "Vegetables":[], "Meat":[], "Seafood":[], "Sweets":[], "Bakery":[]}
        for i in items_list:
            if i.Category == 1:
                categories["Fruits"].append(i)
            elif i.Category == 2:
                categories["Vegetables"].append(i)
            elif i.Category == 3:
                categories["Meat"].append(i)
            elif i.Category == 4:
                categories["Seafood"].append(i)
            elif i.Category == 5:
                categories["Sweets"].append(i)
            elif i.Category == 6:
                categories["Bakery"].append(i)
        for i in categories:
            print(f"{list(categories.keys()).index(i)+1})",i.upper())
        return categories
#------- Function to filter the items depending on user requirements +
def item_list_viewer(inventory_items, task, company):
    categories = item_list_viewer_category(inventory_items, company)
    while True:
        try:
            category_select = int(input(f"Which category would you like {task}(type {len(list(categories.keys()))+1} to restart the program): "))
            if category_select == len(list(categories.keys()))+1:
                os.system("py main.py")
            if category_select in range(len(list(categories.keys()))+1):
                break
            else:
                raise Exception
        except:
            print("Enter a number from one of the option")
    items_list =  categories[list(categories.keys())[category_select-1]]
    print(f"The list of {list(categories.keys())[category_select-1]} available in the inventory are:")
    for i in range(len(items_list)):
        print(f"{i+1}) {items_list[i].Description}")
    
    return items_list
#------- Function to give the user the option to select an item to either edit or view the propeties of. +
def item_selector(task, inventory_items, company):
    
    items_list = item_list_viewer(inventory_items, "open", company)

    while True:
        try:
            user_opt = int(input(f"Which item's properties would you like to {task} from the above list(type {len(items_list)+1} to restart the program): "))
            if user_opt == len(items_list)+1:
                os.system("py main.py")
            if user_opt > len(items_list):
                raise Exception
            break
        except:
            print(f"Please enter a number between 1 and {len(items_list)+1}.")
    print(f"You have selected {items_list[user_opt-1].Description}")
    # os.system('cls')
    
    return items_list[user_opt-1]
#------- Function to update the newly updated inventory objects into the csv file. +
def update_csv(inventory_items, company):
    if company == 1:
        file = open("csv_files/gaming_inventory.csv", "w")
        writy = csv.writer(file, lineterminator="\r")
        writy.writerow(["ItemID","Description","Quantity","ReorderLevel","ReorderQuantity", "Category","UnitCost","TotalValue","Supplier", "Specs","DateLastUpdated","CriticalLevel", "Sold_items", "Earned"])
        for i in inventory_items:
            writy.writerow(i.return_list())
        file.close()
    elif company == 2:
        file = open("csv_files/foods_inventory.csv", "w")
        writy = csv.writer(file, lineterminator="\r")
        writy.writerow(["ItemID","Description","Quantity","ReorderLevel","ReorderQuantity","Category","UnitCost","TotalValue","Supplier","Production_Date","Expiration_Date","CriticalLevel", "Sold_items", "Earned"])
        for i in inventory_items:
            writy.writerow(i.return_list())
        file.close
#------- Function to list the different categories available in the inventory + 
def categories_lister(company):
    if company == 1:
        print("------------------------------------------------------------- \n The list of different categories available are: ")
        with open("csv_files/gaming_categories.csv") as file:
            read = list(csv.reader(file))
        read.pop(0)
        categories = []
        for i in (read):
            categories.append(i[1])

        for i in categories:
            print(f"{(categories).index(i)+1})",i.upper())
        print("-------------------------------------------------------------")
    elif company == 2:
        print("------------------------------------------------------------- \n The list of different categories available are: ")
        with open("csv_files/foods_categories.csv") as file:
            read = list(csv.reader(file))
        read.pop(0)
        categories = []
        for i in (read):
            categories.append(i[1])

        for i in categories:
            print(f"{(categories).index(i)+1})",i.upper())
        print("-------------------------------------------------------------")
#-------Function to create a new category if it doesn't already exist +
def new_category(company):
    if company == 1:
        with open("csv_files/gaming_categories.csv") as file:
            read = list(csv.reader(file))
    elif company == 2:
        with open("csv_files/foods_categories.csv") as file:
            read = list(csv.reader(file))
    read.pop(0)
    num = []
    for i in (read):
        num.append(int(i[0]))
    print(f"The new category number is {num[-1]+1}")
    while True:
        try:
            category_name = input("Enter the category name: ")
            if category_name in [" ", ""]:
                raise Exception
            break
        except:
            print("Invalid Category name.")
    if company == 1:
        with open("csv_files/gaming_categories.csv", "a") as file:
            writ = csv.writer(file, lineterminator="\r")
            writ.writerow([num[-1]+1, category_name])
    elif company == 2:
        with open("csv_files/foods_categories.csv", "a") as file:
            writ = csv.writer(file, lineterminator="\r")
            writ.writerow([num[-1]+1, category_name])
    return num[-1]+1
#---------------------------------------- UPDATE +
def update_objects(inventory_items, company):
    user_update_request = item_selector("edit", inventory_items, company)
    items_list = ["Quantity","ReorderLevel","ReorderQuantity","UnitCost","Supplier","CriticalLevel"]

    print(f"The list of columns that you can update for the item {user_update_request.Description} are:")
    for i in range(len(items_list)):
        print(f"{i+1}) {items_list[i]}")
    while True:
        try:
            user_opt = int(input(f"Which Column would you like to update/edit (type {len(items_list)+1} to restart the program): "))
            if user_opt == len(items_list)+1:
                os.system("py main.py")
            if user_opt > len(items_list):
                raise Exception
            break
        except:
            print(f"Please enter a number between 1 and {len(items_list)}.")
    for i in inventory_items:
        if user_update_request.Description in i.return_list():
            
            if user_opt == 1:
                print(f"The old value of Quantity is {i.Quantity}")
                while True:
                    try:
                        update_val = int(input("Enter the new value: "))
                        if update_val<= 0 or update_val < i.ReorderLevel:
                            print("The Quantity cannot be less than 0 or less than the Reorder Level which is"\
                                  f" {i.ReorderLevel}")
                            raise Exception
                        break
                    except:
                        print("Please enter a non negetive integer")
                i.Quantity = update_val
                i.TotalValue = float(i.UnitCost) * float(i.Quantity)
                
            elif user_opt == 2:
                print(f"The old value of Reorder Level is {i.ReorderLevel}")
                while True:
                    try:
                        update_val = int(input("Enter the new value for Reorder Level: "))
                        if update_val <= 0:
                            raise Exception
                        break
                    except:
                        print("Please enter a non negetive integer")
                i.ReorderLevel = update_val
                
            elif user_opt == 3:
                print(f"The old value for Reorder Quantity is {i.ReorderQuantity}")
                while True:
                    try:
                        update_val = int(input("Enter the new value for Reorder Quantity: "))
                        if update_val<= 0 or update_val < i.ReorderLevel:
                            print("The Quantity cannot be less than 0 or less than the Reorder Level which is"\
                                  f" {i.ReorderLevel}")
                            raise Exception
                        break
                    except:
                        print("Please enter a non negetive integer")
                i.ReorderQuantity = update_val
                
            elif user_opt == 4:
                print(f"The old value for Unit Cost is {i.UnitCost}")
                while True:
                    try:
                        update_val = int(input("Enter the new value for Unit Cost: "))
                        if update_val <= 0:
                            raise Exception
                        break
                    except:
                        print("Please enter a non negetive integer")
                i.UnitCost = update_val
                i.TotalValue = float(i.UnitCost) * float(i.Quantity)
                
            elif user_opt == 5:
                print(f"The old Supplier was {i.Supplier}")
                while True:
                    try:
                        update_val = input("Enter the name of the New Supplier: ")
                        if update_val in ["", " "]:
                            update_val = "N/A"
                        break
                    except:
                        print("Please enter a valid String")
                i.Supplier = update_val
                
            elif user_opt == 6:
                print(f"The old value of Critical Level is {i.CriticalLevel}")
                while True:
                    try:
                        update_val = int(input("Enter the new value: "))
                        if update_val<= 0 or update_val < i.ReorderLevel:
                            print("The Quantity cannot be less than 0 or less than the Reorder Level which is"\
                                  f" {i.ReorderLevel}")
                            raise Exception
                        break
                    except:
                        print("Please enter a non negetive integer")
                i.CriticalLevel = update_val
            if company==1:
                i.DateLastUpdated = datetime.strftime(datetime.now(), "%Y-%m-%d")
            update_csv(inventory_items, company)
    return user_update_request.Description
#---------------------------------------- PROPERTIES +
def properties_viewer(inventory_items, company):
    properties_view_request = item_selector("view", inventory_items, company)
    for i in inventory_items:
        if properties_view_request.Description in i.return_list():
            print(i.__str__())
#---------------------------------------- REORDER
def reorder_checker(inventory_items):
    reorder_list = []
    reorder_list.append(["Description", "Reorder Level", "Quantity", "Default Reorder Quantity"])
    for i in inventory_items:
        if int(i.Quantity) < int(i.ReorderLevel):
            reorder_list.append([i.Description, i.ReorderLevel, i.Quantity, i.ReorderQuantity])
    
    if len(reorder_list) != 1:
        print("The list of items that need to be reordered are: ")
        index_table = []
        for i in range(len(reorder_list)):
            index_table.append(str(i+1))
        index_table.pop(-1)
        print(tabulate.tabulate(reorder_list[1:], headers=reorder_list[0], showindex=index_table , tablefmt="heavy_outline"))
        reorder_opt = continuer("Reorder new stock for the items")
        if reorder_opt == 1:
            while True:
                try:
                    default_or_custom = int(input("Would you like to reorder the default quantities set? (1 for yes and 0 for no): "))
                    break
                except:
                    print("Please Enter a 1 for yes and 0 for no")
            if default_or_custom == 1:
                reorder_default(inventory_items, reorder_list)
            elif default_or_custom == 0:
                reorder_custom(inventory_items, reorder_list)
        else:
            pass
    else:
        print("No stocks need to be reordered ")
        # reorder_list.append(["Description", "ReorderLevel", "Quantity"])
        for i in inventory_items:
            reorder_list.append([i.Description, i.ReorderLevel, i.Quantity, i.ReorderQuantity])
        index_table = []
        for i in range(len(reorder_list)):
            index_table.append(str(i+1))
        index_table.pop(-1)
        print(tabulate.tabulate(reorder_list[1:], headers=reorder_list[0], showindex=index_table , tablefmt="heavy_outline"))
    return index_table
#---------------------------------------- REORDER DEFAULT
def reorder_default(inventory_items, index_list, company):
    for j in range(len(index_list)):
        for i in inventory_items:
            if i.Description == index_list[j][0]:
                i.Quantity += i.ReorderQuantity
    update_csv(inventory_items, company)
#---------------------------------------- REORDER CUSTOM
def reorder_custom(inventory_items, index_list, company):
    for j in range(len(index_list)):
        for i in inventory_items:
            if i.Description == index_list[j][0]:
                while True:
                    try:
                        custom_reorder_quantity = int(input(f"Enter the amount of items you would like to add for {i.Description}: "))
                        if custom_reorder_quantity + i.Quantity > i.ReorderLevel:
                            i.Quantity += custom_reorder_quantity
                        else:
                            print("More stock must be ordered")
                            raise Exception   
                        break
                    except:
                        print("Please Enter a valid value greater than Quantity")
                if custom_reorder_quantity + i.Quantity > i.ReorderLevel:
                    i.Quantity += custom_reorder_quantity
                else:
                    print("More stock must be ordered")                
    update_csv(inventory_items, company)
#---------------------------------------- ADD ITEM
def add_item(inventory_items, company):
    # ------ Description
    while True:
        try:
            Description = input("Enter the name of the item: ")
            if Description == "" or Description == " " or Description.isdigit():
                raise Exception
            break
        except:
            print("Invalid name entered")
    # ------ Quantity
    while True:
        try:
            Quantity = int(input("Enter the Quantity ordered: "))
            if Quantity<=15:
                raise Exception
            break
        except:
            print("The Quantity must be a non negetive integer greater than 15")
    # ------ Reorder level
    while True:
        try:
            user_opt = int(input("Would you like the machine to decide the Reorder Level? (1 for yes and 0 for no): "))
            break
        except:
            print("Please enter 1 for yes and 0 for no")
    ReorderLevel = 0
    CriticalLevel = 0
    if user_opt == 1:
        ReorderLevel = int(Quantity/4)
        print(f"The reorder level set by the machine is {ReorderLevel}")
        CriticalLevel = int(ReorderLevel/3)
    elif user_opt == 0:
        while True:
            try:
                ReorderLevel = int(input("Enter the level at which new stock needs to be reordered:"))
                if ReorderLevel < 0:
                    raise Exception
                break
            except:
                print("The Reorder level must be a non negetive integer")
        CriticalLevel = int(ReorderLevel/3)
    # ------ Reorder Quantity
    while True:
        try:
            ReorderQuantity = int(input("Enter the default quantity to be reordered when the Quantity reaches the Reorder level: ") )
            if ReorderQuantity<ReorderLevel:
                raise Exception
            break
        except:
            print("Please enter a non negetive integer greater than the Reorder level")
    categories_lister(company)
    print("If the category of the item is not listed above then type #")
    while True:
        try:
            Category = input("Enter the category of the item based on the above list: ")
            if Category == "#":
                print("Moving to new Category creation wizard!")
                Category = new_category()
            elif Category.isdigit == False:
                raise Exception
            break
        except:
            print("Please one the number of one of the categories listed above:")
    while True:
        try:
            UnitCost = int(input(f"Enter the cost of one {Description}:"))
            if UnitCost == 0:
                raise ConnectionError
            if UnitCost < 0:
                raise Exception
            break
        except ConnectionError:
            print("The price can't be 0.")
        except:
            print("Please enter a Non negetive integer")
    Supplier = input(f"Enter the supplier of the {Description}: ")
    if Supplier in ["", " "]:
        Supplier = "N/A"
    TotalValue = UnitCost * Quantity 
    DateLastUpdated = datetime.strftime(datetime.now(), "%Y-%m-%d")
    ItemID = int(inventory_items[-1].return_list()[0]) + 1
    Production_Date = datetime.strftime(datetime.now(), "%Y-%m-%d")
    dater = Production_Date.split("-")
    Year = dater[0]
    month = dater[1]
    day = dater[2]
    Expiration_Date = date(int(Year),int(month),int(day)) + relativedelta(years=2, day=1)
    if company == 1:
        print(f"Please enter the Specs of {Description} manually in the csv file in the empty space.")
        headers = ["ItemID","Description","Quantity","ReorderLevel"," Category","UnitCost","TotalValue","Supplier"]
        rows = [[ItemID,Description,Quantity,ReorderLevel,Category,UnitCost,TotalValue,Supplier]]
        row = Gaming_company(ItemID,Description,Quantity,ReorderLevel,ReorderQuantity,Category,UnitCost,TotalValue,Supplier,"",DateLastUpdated,int(CriticalLevel), 0, 0)
        print(tabulate.tabulate(rows, headers=headers , tablefmt="heavy_outline"))
        inventory_items.append(row)
        with open("csv_files/gaming_inventory.csv", "w") as file:
            writ = csv.writer(file, lineterminator="\r")
            writ.writerow(["ItemID","Description","Quantity","ReorderLevel","ReorderQuantity", "Category","UnitCost","TotalValue","Supplier", "Specs","DateLastUpdated","CriticalLevel", "Sold_items","Earned"])
            for i in inventory_items:
                writ.writerow(i.return_list())
    elif company == 2:
        headers = ["ItemID", "Description", "Quantity", "ReorderLevel", "ReorderQuantity", "Category", "UnitCost", "TotalValue", "Supplier", "Production_Date", "Expiration_Date"]
        rows = [[ItemID,Description,Quantity,ReorderLevel,ReorderQuantity,Category,UnitCost,TotalValue,Supplier]]
        row = Food_company(ItemID, Description,Quantity, ReorderLevel, ReorderQuantity, Category, UnitCost, TotalValue, Supplier, Production_Date, Expiration_Date, CriticalLevel, 0, 0)
        inventory_items.append(row)
        print(tabulate.tabulate(rows, headers=headers , tablefmt="heavy_outline"))

        with open("csv_files/foods_inventory.csv", "w") as file:
            writ = csv.writer(file, lineterminator="\r")
            writ.writerow(["ItemID","Description","Quantity","ReorderLevel","ReorderQuantity","Category","UnitCost","TotalValue","Supplier","Production_Date","Expiration_Date","CriticalLevel","Sold_items","Earned"])
            for i in inventory_items:
                writ.writerow(i.return_list())
#---------------------------------------- SELL ITEM
def Sold_items(inventory_items, company):
    print("Update Sold items")
    user_update_request = item_selector("edit", inventory_items, company)
    print(f"The Quantity present in stock is {user_update_request.Quantity}")
    while True:
        try:
            ammount_sold = int(input("Enter the amount of items sold: "))
            if ammount_sold > user_update_request.Quantity:
                print(f"The Quantity present in stock is {user_update_request.Quantity}")
                raise Exception
            else:
                break
        except:
            print("Please enter a valid ammount")
    user_update_request.Quantity -= ammount_sold
    user_update_request.Sold_items += ammount_sold
    user_update_request.Earned = int(ammount_sold * user_update_request.UnitCost)
    update_csv(inventory_items, company)