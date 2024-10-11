#Define the menu of the restaurant
menu = {
    'Pizza':120,
    'Pasta':100,
    'Burger':85,
    'Salad':50,
    'Coffee':30,
}
print("Welcome to MY RESTAURANT")
print("\nPizza: Rs120\nPasta: Rs100\nBurger: 85\nSalad: 50\nCoffee: 30")

order_total = 0
item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to the order")
else:
    print("Sorry, we don't have this item in our menu")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of item you want to order = ")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available")
print(f"The total amount of items to pay is {order_total}")