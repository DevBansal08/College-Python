cart = {}

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    if name in cart.keys():  
        cart[name]["quantity"] += quantity 
    else:
        cart[name] = {"price": price, "quantity": quantity}
    
    print("Added", quantity, "x", name, "to cart.")

def remove_item():
    name = input("Enter item name to remove: ")
    if name in cart.keys():
        cart.pop(name)
        print("Removed", name, "from cart.")
    else:
        print("Item not found in cart!")

def update_quantity():
    name = input("Enter item name to update: ")
    if name in cart.keys():
        quantity = int(input("Enter new quantity: "))
        if quantity > 0:
            cart[name]["quantity"] = quantity
            print("Updated", name, "quantity to", quantity)
        else:
            cart.pop(name)
            print("Removed", name, "as quantity is now zero.")
    else:
        print("Item not found in cart!")

def display_cart():
    if not cart:
        print("Your cart is empty!")
        return
    
    total = 0
    print("\n🛙 Shopping Cart:")
    for name, details in cart.items():
        cost = details["price"] * details["quantity"]
        total += cost
        print("-", name + ":", details["quantity"], "x $", f"{details['price']:.2f}", "=", "$", f"{cost:.2f}")
    print("\n Total Cost:", "$", f"{total:.2f}")

def checkout():
    display_cart()
    if cart:
        cart.clear()
        print("\n Checkout successful! Thank you for shopping.")
    else:
        print("Your cart is empty!")

while True:
    print("\n Shopping Cart Menu:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Update Quantity")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    match choice:
        case "1":
            add_item()
        case "2":
            remove_item()
        case "3":
            update_quantity()
        case "4":
            display_cart()
        case "5":
            checkout()
        case "6":
            print("Exiting program. Goodbye!")
            break
        case _:
            print("Invalid choice! Please enter a number between 1 and 6.")



