import csv
from datetime import *
class Inventory:
    def __init__(self, ItemID,Description,Quantity,ReorderLevel,ReorderQuantity, Category,UnitCost,TotalValue,Supplier,CriticalLevel, Sold_items, Earned):
        self.ItemID = ItemID
        self.Description = Description
        self.Quantity = Quantity
        self.ReorderLevel = ReorderLevel
        self.ReorderQuantity = ReorderQuantity
        self.Category = Category
        self.UnitCost = UnitCost
        self.TotalValue = TotalValue
        self.Supplier = Supplier
        self.CriticalLevel = CriticalLevel
        self.Sold_items = Sold_items
        self.Earned = Earned
    
    def get_index(self, column):
        if column in ("ItemID", 1):
            return 0
        elif column in ("Description", 2):
            return 1
        elif column in ("Quantity", 3):
            return 2
        elif column in ("ReorderLevel", 4):
            return 3
        elif column in ("ReorderQuantity", 5):
            return 4
        elif column in ("UnitCost", 6):
            return 5
        elif column in ("TotalValue", 7):
            return 6
        elif column in ("Supplier", 8):
            return 7
        elif column in ("DateLastUpdated", 9):
            return 8
        elif column in ("CriticalLevel", 10):
            return 9
        else:
            return None  
    def reorder_requirement(self):
        if self.Quantity < self.ReorderLevel:
            if self.Quantity > self.CriticalLevel:
                return f"More stock need to be purchased as company is short"\
            f" of stock by {self.ReorderLevel - self.Quantity}"
            else:
                return f"THe critical level has been reached and new stock must be purchased to avoid any issues"
        else:
            return f"There is still {self.Quantity - self.ReorderLevel} items in stock"\
                " before new stock is required"
    def __str__(self):
        return f"Item: {self.Description} \n"\
            f"{self.reorder_requirement()}\n"\
            f"Cost for one unit is {self.UnitCost} \nThere are a total of {self.Quantity} {self.Description}'s in stock at the moment\n"\
            

class Gaming_company(Inventory):
    def __init__(self, ItemID,Description,Quantity,ReorderLevel,ReorderQuantity, Category,UnitCost,TotalValue,Supplier, Specs,DateLastUpdated,CriticalLevel, Sold_items, Earned):
        super().__init__(ItemID,Description,Quantity,ReorderLevel,ReorderQuantity, Category,UnitCost,TotalValue,Supplier,CriticalLevel, Sold_items, Earned)
        self.Specs = Specs
        self.DateLastUpdated = DateLastUpdated
    def return_list(self):
        return [self.ItemID,self.Description,self.Quantity,self.ReorderLevel,self.ReorderQuantity, self.Category,self.UnitCost,self.TotalValue,self.Supplier, self.Specs, self.DateLastUpdated,self.CriticalLevel, self.Sold_items, self.Earned]
    def short_Specs(self):
        specifications = self.Specs
        specs_list = specifications.split(",")
        str_specs = ""
        for i in specs_list:
            str_specs += i.strip() + "\n"
        return str_specs
    def __str__(self):
        return super().__str__() + f"The item's properties was last updated on {self.DateLastUpdated}"\
        f"\n specifications of {self.Description}: \n"\
        f"{self.short_Specs()}"
    
class Food_company(Inventory):
    def __init__(self, ItemID,Description,Quantity,ReorderLevel,ReorderQuantity,Category,UnitCost,TotalValue,Supplier,Production_Date,Expiration_Date,CriticalLevel, Sold_items, Earned):
        super().__init__(ItemID,Description,Quantity,ReorderLevel,ReorderQuantity, Category,UnitCost,TotalValue,Supplier,CriticalLevel, Sold_items, Earned)
        self.Production_Date = Production_Date
        self.Expiration_Date = Expiration_Date
    def return_list(self):
        return [self.ItemID,self.Description,self.Quantity,self.ReorderLevel,self.ReorderQuantity, self.Category,self.UnitCost,self.TotalValue,self.Supplier,self.Production_Date,self.Expiration_Date,self.CriticalLevel, self.Sold_items, self.Earned]
    def check_date_expired(self):
        if datetime.strftime(datetime.now(), "%Y") <= "2023":
            if datetime.strftime(datetime.now(), "%m") <= "12":
                if datetime.strftime(datetime.now(), "%d") <= "22":
                    print(False)
                else:
                   return True
            else:
                return True
        else:
            return True
    def __str__(self):
        return super().__str__() + f"The Production date of {self.Description} is: {self.Production_Date}"\
        f"\nThe Expiration date is: {self.Expiration_Date}"