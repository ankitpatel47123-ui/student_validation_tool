orders = []
subtotal = 0
while True:
    print("\n======= SMART CANTEEN =======")
    print("1. Veg Sandwich - Rs. 60")
    print("2. Masala Dosa - Rs. 80")
    print("3. Chole Rice - Rs. 90")
    print("4. Paneer Roll - Rs. 100")
    print("5. Tea - Rs. 20")

    choice = int(input("Choose item number: "))
    if choice == 1:
        item = "Veg Sandwich"
        price = 60
    elif choice == 2:
        item = "Masala Dosa"
        price = 80
    elif choice == 3:
        item = "Chole Rice"
        price = 90
    elif choice == 4:
        item = "Paneer Roll"
        price = 100
    elif choice == 5:
        item = "Tea"
        price = 20
    else:
        print("Invalid Item Number")
        continue
    quantity = int(input("Enter Quantity: "))
    if quantity <= 0:
        print("Quantity Must Be Positive")
        continue
    totalcost = price * quantity
    subtotal = subtotal + totalcost
    orders.append([item, quantity, totalcost])
    print("Added:", item, "x", quantity, "= Rs.", totalcost)
    more = input("Add Another Item? (y/n): ")
    if more.lower() != "y":
        break
print("\n======= RECEIPT =======")
for order in orders:
    print(order[0], "x", order[1], ": Rs.", order[2])

if subtotal >= 500:
    discount = subtotal * 10 / 100
elif subtotal >= 250:
    discount = subtotal * 5 / 100
else:
    discount = 0
finaltotal = subtotal - discount
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final Total:", finaltotal)
print("Thank You!")