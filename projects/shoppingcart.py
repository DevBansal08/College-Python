class shopping:
    def __init__(self):
        self.cart = {}

    def add_item(self):
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))

        if name in self.cart.keys():  
             self.cart[name]["quantity"] += quantity 
             self.cart[name]["price"] = price 
        else:
            self.cart[name] = {"price": price, "quantity": quantity}
    
        print("Added", quantity, "x", name, "to cart.")

    def remove_item(self):
        name = input("Enter item name to remove: ")
        if name in self.cart.keys():
            self.cart.pop(name)
            print("Removed", name, "from cart.")
        else:
             print("Item not found in cart!")

    def update_quantity(self):
       name = input("Enter item name to update: ")
       if name in self.cart.keys():
            quantity = int(input("Enter new quantity: "))
            if quantity > 0:
                self.cart[name]["quantity"] = quantity
                print("Updated", name, "quantity to", quantity)
            else:
                self.cart.pop(name)
                print("Removed", name, "as quantity is now zero.")
       else:
            print("Item not found in cart!")

    def display_cart(self):
        if not self.cart:
            print("Your cart is empty!")
            return
    
        total = 0
        print("\n🛙 Shopping Cart:")
        for name, details in self.cart.items():
            cost = details["price"] * details["quantity"]
            total += cost
            print("-", name + ":", details["quantity"], "x $", f"{details['price']:.2f}", "=", "$", f"{cost:.2f}")
        print("\n Total Cost:", "$", f"{total:.2f}")

    def checkout(self):
        self.display_cart()
        if self.cart:
            self.cart.clear()
            print("\n Checkout successful! Thank you for shopping.")
        else:
            print("Your cart is empty!")

    def menu(self):
        while True:
            print("\nShopping Cart Menu:")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. Update Quantity")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            match choice:
                case "1":
                    self.add_item()
                case "2":
                    self.remove_item()
                case "3":
                    self.update_quantity()
                case "4":
                    self.display_cart()
                case "5":
                    self.checkout()
                case "6":
                    print("Exiting program. Goodbye!")
                    break  
                case _:
                    print("Invalid choice! Please enter a number between 1 and 6.")

cls=shopping()
cls.menu()


