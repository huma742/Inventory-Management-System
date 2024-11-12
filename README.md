### **Explanation of Code**

This code defines an Inventory Management System (IMS) that allows both administrators and regular users to perform various tasks related to product management. The code consists of two main classes: **`Product`** and **`InventoryManagementSystem`**, which work together to simulate an inventory system where products can be added, edited, deleted, viewed, and searched. Here's a breakdown of the different components of the code:



### **1. `Product` Class**

The `Product` class represents a product in the inventory. It contains attributes and methods to manage product information.

#### **Attributes:**
- `product_id`: Unique identifier for each product.
- `name`: Name of the product.
- `category`: Category the product belongs to.
- `price`: Price of the product.
- `stock_quantity`: Current quantity of the product in stock.

#### **Methods:**
- **`__init__`**: Constructor that initializes a product with the given product ID, name, category, price, and stock quantity.
- **`adjust_stock`**: Method to adjust the stock quantity by adding or subtracting a specified quantity.
- **`__str__`**: Method to return a string representation of the product, displaying the product's ID, name, category, price, and stock quantity in a readable format.



### **2. `InventoryManagementSystem` Class**

The `InventoryManagementSystem` class manages the entire inventory, user authentication, and provides the functionality for both users and admins.

#### **Attributes:**
- `products`: A dictionary that stores products with their unique `product_id` as the key.
- `users`: A dictionary that stores users' login credentials and roles (admin or user).

#### **Methods:**
- **`login`**: Validates the user's credentials (username and password). If valid, it returns the role of the user ("admin" or "user"). If invalid, it returns `None`.
- **`add_product`**: Adds a new product to the inventory. It first checks if the `product_id` already exists to avoid duplicates.
- **`edit_product`**: Allows editing an existing product's details (name, category, price, or stock quantity).
- **`delete_product`**: Deletes a product from the inventory by its `product_id`.
- **`view_inventory`**: Displays the list of all products in the inventory.
- **`search_product`**: Searches for products based on name and/or category. It filters the products that match the provided search criteria.
- **`check_stock_levels`**: Displays products that have low stock (default threshold is 5 units).
- **`adjust_stock`**: Adjusts the stock of a specific product by a given quantity (can be positive or negative).
- **`admin_menu`**: Displays an interactive menu for the admin user to manage the inventory (add, edit, delete products, etc.).
- **`user_menu`**: Displays an interactive menu for regular users to view inventory and search for products.
- **`run`**: The main method that initiates the login process and directs the user to either the admin menu or user menu based on their role.



### **3. **User Roles**

The `InventoryManagementSystem` supports two types of users:
1. **Admin**: Has full control over the inventory, including adding, editing, deleting products, checking stock levels, and adjusting stock.
2. **User**: Has limited access and can only view the inventory and search for products.



### **4. Flow of the Program**

The program starts by running the **`ims.run()`** method. Here’s how the flow works:
1. **Login**: The user is prompted to enter a role (`admin` or `user`) and password.
    - If valid credentials are entered, the system logs the user in and displays the appropriate menu based on their role.
    - If invalid credentials are entered, the system denies access.
   
2. **Admin Menu**: Once logged in as an admin, the admin can perform tasks such as:
    - View inventory
    - Add products
    - Edit products
    - Delete products
    - Check stock levels
    - Adjust stock quantities
    - Log out

### **3.User Menu**: 
     Once logged in as a user, the user can perform the following tasks:
    - View the entire inventory
    - Search for products based on name or category
    - Log out

 ### **4. Product Management**: 
     For both admins and users, the `Product` class is used to manage product attributes and manipulate stock levels. Admins have full access to modify products, whereas users have only view and search capabilities.



### **5. Error Handling**

- The program ensures that the `product_id` is unique when adding a new product.
- Input validation is performed for product price and stock quantities. If the user enters invalid data (like a string when a number is expected), it raises an error message and requests valid input.
- The system checks if a product exists before performing operations like editing, deleting, or adjusting stock.



### **6. Key Points**

- **Product Addition**: New products are added to the system by the admin. Each product is assigned a unique `product_id` and is stored in the `products` dictionary.
- **Product Update**: Admins can modify the product details through the `edit_product` method, updating attributes such as name, category, price, and stock quantity.
- **Stock Adjustment**: Admins can adjust the stock of a product by adding or subtracting quantities using the `adjust_stock` method.
- **User Experience**: Regular users can only view the products and search for specific items without modifying the inventory.



### **Conclusion**

This code provides a basic but functional inventory management system with user authentication and two distinct roles (admin and user). It allows admins to manage product data and stock levels, while users can interact with the inventory by viewing and searching products.
