print("========================================")
print("      SALES RECORD MANAGEMENT SYSTEM    ")
print("========================================")
print("1. Add Sale Record")
print("2. View All Records & Summary Statistics")
print("3. Clear All Sales Data")
print("4. Exit System")
print("========================================")

def Item_Name ():
    return input("Input the item name: ")

def Quantity_Sold () :
   return int(input("Input the quantity sold: "))

def Price_Per_Unit () :
    return float(input("Input price per unit: "))

def Exit_System () :
    exit('Thank you for using the Sales Record Management System.')


option_menu = input("Select an option (1-4) : ")


item_name = Item_Name()
quantity_sold = Quantity_Sold()
price_per_unit = Price_Per_Unit()




while True :
    if option_menu == "1" :
        Item_Name()
        Quantity_Sold()
        Price_Per_Unit()
        break
    if option_menu == "4" :
        Exit_System()


#Calculate the total transaction amount
total_amount = Quantity_Sold * Price_Per_Unit

#Print/Display the Item name, Quantity Sold, Price per unit, and Total amount
print(f"Item Name: {item_name}, Quantity: {quantity_sold}, Price Per Unit: {price_per_unit}, Total Amount: {total_amount} ")
print("Sale record saved successfully. ")









