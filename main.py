print("========================================")
print("       SALES RECORD MANAGEMENT SYSTEM")
print("========================================")
print("1. Add Sale Record")
print("2. View All Records & Summary Statistics")
print("3. Clear All Sales Data")
print("4. Exit System")
print("========================================")

def Item_Name ():
    input("Input the item name: ")

def Quantity_Sold () :
   int(input("Input the quantity sold: "))

def Price_Per_Unit () :
    float(input("Input price per unit: "))

def Exit_System () :
    exit('Thank you for using the Sales Record Management System.')


option_menu = input("Select an option (1-4) : ")

while True :
    if option_menu == "1" :
        Item_Name()
        Quantity_Sold()
        Price_Per_Unit()
    if option_menu == "4" :
        Exit_System()


total_amount = Quantity_Sold * Price_Per_Unit




#print(f"Item Name: {Item_Name}, Quantity: {Quantity_Sold}, Price Per Unit: {Price_Per_Unit}, Total Amount: {total_amount} ")
print(Item_Name)
print(Quantity_Sold)





