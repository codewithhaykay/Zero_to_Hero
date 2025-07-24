##This program calculate the total bills of a customer
##based on the quantity of goods bought and the price the 
##goods is sold.

quantity = int(input("Enter the quantity of goods bought: "))
price = float(input("Enter the price: "))
total = quantity * price
print(f'The total amount of goods bought is N{total}')