#Billing system in python 
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class CustomerBillingSystem:
    def __init__(self):
        self.products = []
        self.cart = []

    def add_product(self, name, price):
        product = Product(name, price)
        self.products.append(product)

    def display_products(self):
        print("Available Products:")
        idx = 1  # Initialize a counter
        for product in self.products:
            print(f"{idx}. {product.name} - ${product.price:.2f}")
            idx += 1  # Increment the counter

    def add_to_cart(self, product_idx):
        if 1 <= product_idx <= len(self.products):
            selected_product = self.products[product_idx - 1]
            self.cart.append(selected_product)
            print(f"{selected_product.name} added to cart.")

    def calculate_total(self):
        total = 0
        for product in self.cart:
            total += product.price
        return total

    def generate_bill(self):
        print("\nGenerating Bill...\n")
        idx = 1  # Initialize a counter
        for product in self.cart:
            print(f"{idx}. {product.name} - ${product.price:.2f}")
            idx += 1  # Increment the counter
        total = self.calculate_total()
        print(f"\nTotal: ${total:.2f}")

if __name__ == "__main__":
    billing_system = CustomerBillingSystem()

    billing_system.add_product("Atta 1", 10.99)
    billing_system.add_product("Biscuit 2", 15.49)
    billing_system.add_product("Chocolate 3", 5.25)
    billing_system.add_product("Ghee 4", 29.99)
    
    while True:
        print("\n1. Display Products")
        print("2. Add to Cart")
        print("3. Generate Bill")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            billing_system.display_products()
        elif choice == 2:
            billing_system.display_products()
            product_idx = int(input("Enter the product number to add to cart: "))
            billing_system.add_to_cart(product_idx)
        elif choice == 3:
            billing_system.generate_bill()
            break
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")
