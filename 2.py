''' Assumptions taken :
    Printing all the products(Price per kg) which are available in the budget after exiting the menu. 
'''

import re
def menu():
    print("1. Add an item")
    print("2. Exit")
    choice = int(input("Enter your choice : "))
    return choice

grocery_list = {}
budget = int(input("Enter your budget : "))
choice = menu()
while(choice != 2):
    product = input("\n\nEnter product : ")
    quantity = input("Enter quantity : ")
    price = int(input("Enter price : "))
    print("\n")
    quantity = re.findall('\d*\.?\d+', quantity)             # Extracting integer/float part from quantity
    quantity = list(map(float, quantity))

    if (price > budget):
        print("Can't Buy the product ###(because budget left is {})\n\n".format(budget))
        choice = menu()
        continue

    if (product in grocery_list):
        grocery_list[product][0] += quantity[0]
        grocery_list[product][1] += price 
    else:
        grocery_list[product] = [quantity[0], price]

    budget -= price
    print("Amount left : {}\n\n".format(budget))

    choice = menu() 

print("\n")
if(budget > 0) : 
    for i in grocery_list :
        per_kg_price = grocery_list[i][1]/grocery_list[i][0]
        if( per_kg_price <= budget):
            print("Amount left can buy you", i, "at {} per kg".format(per_kg_price))

print("\n")
print("GROCERY LIST is : \n")
print("Product Name\tQuantity\tPrice")
for i in grocery_list:
    print(i, "\t\t", grocery_list[i][0], "kg\t\t", grocery_list[i][1])