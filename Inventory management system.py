class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def adjust_stock(self, quantity):
        self.stock_quantity += quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: ${self.price:.2f}, Stock: {self.stock_quantity}"


class InventoryManagementSystem:
    def __init__(self):
        self.products = {}
        self.users = {
            "admin": {"password": "adminpassword", "role": "admin"},
            "user": {"password": "userpassword", "role": "user"}
        }

    def login(self, username, password):
        user = self.users.get(username)
        if user and user["password"] == password:
            print(f"Welcome, {username}! Role: {user['role']}")
            return user["role"]
        else:
            print("Invalid credentials.")
            return None

    def add_product(self, product_id, name, category, price, stock_quantity):
        if product_id in self.products:
            print("Product ID already exists.")
        else:
            self.products[product_id] = Product(product_id, name, category, price, stock_quantity)
            print(f"Product '{name}' added successfully.")

    def edit_product(self, product_id, name=None, category=None, price=None, stock_quantity=None):
        product = self.products.get(product_id)
        if product:
            if name:
                product.name = name
            if category:
                product.category = category
            if price is not None:
                product.price = price
            if stock_quantity is not None:
                product.stock_quantity = stock_quantity
            print(f"Product ID '{product_id}' updated successfully.")
        else:
            print("Product not found.")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product ID '{product_id}' deleted successfully.")
        else:
            print("Product not found.")

    def view_inventory(self):
        if not self.products:
            print("Inventory is empty.")
        for product in self.products.values():
            print(product)

    def search_product(self, name=None, category=None):
        found_products = [
            product for product in self.products.values()
            if (name and name.lower() in product.name.lower()) or (category and category.lower() in product.category.lower())
        ]
        if found_products:
            for product in found_products:
                print(product)
        else:
            print("No matching products found.")

    def check_stock_levels(self, low_threshold=5):
        low_stock_products = [product for product in self.products.values() if product.stock_quantity <= low_threshold]
        if low_stock_products:
            print("Products with low stock levels:")
            for product in low_stock_products:
                print(product)
        else:
            print("All products have sufficient stock levels.")

    def adjust_stock(self, product_id, quantity):
        product = self.products.get(product_id)
        if product:
            product.adjust_stock(quantity)
            print(f"Product ID '{product_id}' stock adjusted by {quantity}. New stock: {product.stock_quantity}")
        else:
            print("Product not found.")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. View Inventory")
            print("2. Add Product")
            print("3. Edit Product")
            print("4. Delete Product")
            print("5. Check Stock Levels")
            print("6. Adjust Stock")
            print("7. Log Out")
            choice = input("Choose an option: ")

            if choice == "1":
                self.view_inventory()
            elif choice == "2":
                try:
                    product_id = input("Enter product ID: ")
                    name = input("Enter product name: ")
                    category = input("Enter category: ")
                    price = float(input("Enter price: "))
                    stock_quantity = int(input("Enter stock quantity: "))
                    self.add_product(product_id, name, category, price, stock_quantity)
                except ValueError:
                    print("Invalid input. Please enter valid data.")
            elif choice == "3":
                product_id = input("Enter product ID to edit: ")
                name = input("Enter new name (or leave blank to keep current): ")
                category = input("Enter new category (or leave blank to keep current): ")
                price = input("Enter new price (or leave blank to keep current): ")
                stock_quantity = input("Enter new stock quantity (or leave blank to keep current): ")

                price = float(price) if price else None
                stock_quantity = int(stock_quantity) if stock_quantity else None
                self.edit_product(product_id, name, category, price, stock_quantity)
            elif choice == "4":
                product_id = input("Enter product ID to delete: ")
                self.delete_product(product_id)
            elif choice == "5":
                self.check_stock_levels()
            elif choice == "6":
                try:
                    product_id = input("Enter product ID to adjust stock: ")
                    quantity = int(input("Enter quantity to add/subtract: "))
                    self.adjust_stock(product_id, quantity)
                except ValueError:
                    print("Invalid quantity. Please enter a valid number.")
            elif choice == "7":
                print("Logging out...")
                break
            else:
                print("Invalid option. Try again.")

    def user_menu(self):
        while True:
            print("\nUser Menu:")
            print("1. View Inventory")
            print("2. Search Product")
            print("3. Log Out")
            choice = input("Choose an option: ")

            if choice == "1":
                self.view_inventory()
            elif choice == "2":
                name = input("Enter product name to search (or leave blank to skip): ")
                category = input("Enter category to search (or leave blank to skip): ")
                self.search_product(name=name, category=category)
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid option. Try again.")

    def run(self):
        while True:
            print("\nInventory Management System")
            username = input("Enter Role(user/admin): ")
            password = input("Enter password: ")
            role = self.login(username, password)

            if role == "admin":
                self.admin_menu()
            elif role == "user":
                self.user_menu()
            else:
                print("Access Denied.")


# Initialize and run the system
ims = InventoryManagementSystem()
ims.run()
