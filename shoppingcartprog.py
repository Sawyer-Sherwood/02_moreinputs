item = input("Enter the item you want to buy: ") 
price = float(input("What is the price of the item: ")) 
quantity = int(input("How many of the item do you want to buy: ")) 
total = price * quantity
print(f"The total cost for {quantity} {item}(s) is ${total:.2f}.")