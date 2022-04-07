MIN_ITEM = 0
MAX_PRICE = 100

items = int(input("Number of items: "))
total = 0

while items < MIN_ITEM:
    print("Invalid")
    print("Please enter the number of items again")
    items = int(input("Number of items: "))

for i in range(items):
    price = float(input("Price of item: "))
    total = total + price

if total > MAX_PRICE:
    dis_total = total * 0.1
    print("Total price for", items, " items is $", dis_total)

else:
    print("Total price for", items, " items is $", total)