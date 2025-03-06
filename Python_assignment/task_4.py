import tkinter as tk
from tkinter import messagebox, filedialog
import pickle
from datetime import datetime

# Sample credentials for authentication (username:password)
credentials = {'admin': 'password123', 'user1': 'pass1234'}

# Sample data
inventory = [{'name': 'Product1', 'quantity': 50, 'price': 10.0, 'category': 'Category1'}]
sales_history = []

def authenticate():
    username = entry_username.get()
    password = entry_password.get()

    if username in credentials and credentials[username] == password:
        messagebox.showinfo("Login Success", "Welcome, " + username + "!")
        login_root.withdraw()  # Hide the login window
        open_inventory_system()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_inventory_system():
    global root, listbox_products
    root = tk.Tk()
    root.title("Inventory Management System")

    # Frame for Product Management
    frame_product_management = tk.Frame(root)
    frame_product_management.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    tk.Label(frame_product_management, text="Product Name:").grid(row=0, column=0, padx=5, pady=5)
    entry_name = tk.Entry(frame_product_management)
    entry_name.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_product_management, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
    entry_quantity = tk.Entry(frame_product_management)
    entry_quantity.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_product_management, text="Price:").grid(row=2, column=0, padx=5, pady=5)
    entry_price = tk.Entry(frame_product_management)
    entry_price.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame_product_management, text="Category:").grid(row=3, column=0, padx=5, pady=5)
    entry_category = tk.Entry(frame_product_management)
    entry_category.grid(row=3, column=1, padx=5, pady=5)

    tk.Button(frame_product_management, text="Add Product", command=lambda: add_product(entry_name, entry_quantity, entry_price, entry_category, listbox_products)).grid(row=4, column=0, columnspan=2, pady=10)

    tk.Label(frame_product_management, text="Product ID to delete:").grid(row=5, column=0, padx=5, pady=5)
    entry_delete_id = tk.Entry(frame_product_management)
    entry_delete_id.grid(row=5, column=1, padx=5, pady=5)

    tk.Button(frame_product_management, text="Delete Product", command=lambda: delete_product(entry_delete_id, listbox_products)).grid(row=6, column=0, columnspan=2, pady=10)

    # Frame for Search and Sales
    frame_search_sales = tk.Frame(root)
    frame_search_sales.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    tk.Label(frame_search_sales, text="Search Product:").grid(row=0, column=0, padx=5, pady=5)
    entry_search = tk.Entry(frame_search_sales)
    entry_search.grid(row=0, column=1, padx=5, pady=5)

    tk.Button(frame_search_sales, text="Search", command=lambda: search_product(entry_search, listbox_products)).grid(row=1, column=0, columnspan=2, pady=10)

    tk.Label(frame_search_sales, text="Product ID:").grid(row=2, column=0, padx=5, pady=5)
    entry_product_id = tk.Entry(frame_search_sales)
    entry_product_id.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame_search_sales, text="Quantity:").grid(row=3, column=0, padx=5, pady=5)
    entry_quantity_sale = tk.Entry(frame_search_sales)
    entry_quantity_sale.grid(row=3, column=1, padx=5, pady=5)

    tk.Button(frame_search_sales, text="Record Sale", command=lambda: record_sale(entry_product_id, entry_quantity_sale, listbox_products)).grid(row=4, column=0, columnspan=2, pady=10)

    # Frame for Reports
    frame_reports = tk.Frame(root)
    frame_reports.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    tk.Button(frame_reports, text="Daily Sales Report", command=daily_sales_report).grid(row=0, column=0, pady=10)
    tk.Button(frame_reports, text="Top Selling Products", command=top_selling_products).grid(row=0, column=1, pady=10)
    tk.Button(frame_reports, text="Revenue Analysis", command=revenue_analysis).grid(row=0, column=2, pady=10)

    # Frame for Backup and Restore
    frame_backup_restore = tk.Frame(root)
    frame_backup_restore.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    tk.Button(frame_backup_restore, text="Backup Data", command=backup_data).grid(row=0, column=0, pady=10)
    tk.Button(frame_backup_restore, text="Restore Data", command=lambda: restore_data(listbox_products)).grid(row=0, column=1, pady=10)

    # Listbox for displaying products
    listbox_products = tk.Listbox(root, width=100)
    listbox_products.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    update_product_list(listbox_products)
    root.mainloop()

def add_product(entry_name, entry_quantity, entry_price, entry_category, listbox_products):
    name = entry_name.get()
    quantity = entry_quantity.get()
    price = entry_price.get()
    category = entry_category.get()

    if name and quantity.isdigit() and price.replace('.', '', 1).isdigit() and category:
        product = {
            'name': name,
            'quantity': int(quantity),
            'price': float(price),
            'category': category
        }
        inventory.append(product)
        messagebox.showinfo("Product Added", "Product has been added successfully")
        clear_entries(entry_name, entry_quantity, entry_price, entry_category)
        update_product_list(listbox_products)
    else:
        messagebox.showerror("Input Error", "Please enter valid product details")

def delete_product(entry_delete_id, listbox_products):
    try:
        product_id = int(entry_delete_id.get())
        if 0 <= product_id < len(inventory):
            del inventory[product_id]
            messagebox.showinfo("Product Deleted", "Product has been deleted successfully")
            clear_entries(entry_delete_id)  # Changed from entry_delete_id=entry_delete_id
            update_product_list(listbox_products)
        else:
            messagebox.showerror("Invalid ID", "Product ID does not exist")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid product ID")

def search_product(entry_search, listbox_products):
    search_query = entry_search.get().lower()
    listbox_products.delete(0, tk.END)
    
    for idx, product in enumerate(inventory):
        if search_query in product['name'].lower() or search_query in product['category'].lower():
            listbox_products.insert(tk.END, f"ID: {idx} - {product['name']}, Quantity: {product['quantity']}, Price: {product['price']}, Category: {product['category']}")

def record_sale(entry_product_id, entry_quantity_sale, listbox_products):
    product_id = int(entry_product_id.get())
    quantity = int(entry_quantity_sale.get())

    if 0 <= product_id < len(inventory):
        product = inventory[product_id]
        if product['quantity'] >= quantity:
            product['quantity'] -= quantity
            sale = {
                'product_name': product['name'],
                'quantity': quantity,
                'total_price': quantity * product['price'],
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            sales_history.append(sale)
            messagebox.showinfo("Sale Recorded", f"Sale of {quantity} units of {product['name']} recorded.")
            update_product_list(listbox_products)
        else:
            messagebox.showerror("Error", "Not enough stock available.")
    else:
        messagebox.showerror("Error", "Invalid Product ID.")

def daily_sales_report():
    today = datetime.now().date()
    total_sales = sum(sale['total_price'] for sale in sales_history if datetime.strptime(sale['timestamp'], '%Y-%m-%d %H:%M:%S').date() == today)
    messagebox.showinfo("Daily Sales Report", f"Total sales for today: ${total_sales:.2f}")

def top_selling_products():
    product_sales = {}
    for sale in sales_history:
        product_name = sale['product_name']
        product_sales[product_name] = product_sales.get(product_name, 0) + sale['quantity']

    sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)
    top_products = '\n'.join([f"{product}: {quantity} units sold" for product, quantity in sorted_products[:5]])

    messagebox.showinfo("Top Selling Products", f"Top 5 selling products:\n{top_products}")

def revenue_analysis():
    revenue = sum(sale['total_price'] for sale in sales_history)
    messagebox.showinfo("Revenue Analysis", f"Total revenue: ${revenue:.2f}")

def backup_data():
    file_path = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Pickle Files", "*.pkl")])
    if file_path:
        with open(file_path, 'wb') as file:
            pickle.dump({'inventory': inventory, 'sales_history': sales_history}, file)
        messagebox.showinfo("Backup Success", "Data backed up successfully")

def restore_data(listbox_products):
    file_path = filedialog.askopenfilename(filetypes=[("Pickle Files", "*.pkl")])
    if file_path:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            global inventory, sales_history
            inventory = data.get('inventory', [])
            sales_history = data.get('sales_history', [])
            messagebox.showinfo("Restore Success", "Data restored successfully")
            update_product_list(listbox_products)

def clear_entries(*entries):
    for entry in entries:
        entry.delete(0, tk.END)

def update_product_list(listbox):
    listbox.delete(0, tk.END)
    for idx, product in enumerate(inventory):
        listbox.insert(tk.END, f"ID: {idx} - {product['name']}, Quantity: {product['quantity']}, Price: {product['price']}, Category: {product['category']}")
        
def record_sale(entry_product_id, entry_quantity_sale, listbox_products):
    try:
        product_id = int(entry_product_id.get())
        quantity = int(entry_quantity_sale.get())

        if 0 <= product_id < len(inventory):
            product = inventory[product_id]
            if product['quantity'] >= quantity:
                product['quantity'] -= quantity
                sale = {
                    'product_name': product['name'],
                    'quantity': quantity,
                    'total_price': quantity * product['price'],
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                sales_history.append(sale)
                messagebox.showinfo("Sale Recorded", f"Sale of {quantity} units of {product['name']} recorded.")
                
                # Check if the product quantity is below the threshold
                if product['quantity'] < 10:
                    messagebox.showwarning("Low Stock Alert", f"The quantity of {product['name']} is below 10 units!")
                
                update_product_list(listbox_products)
            else:
                messagebox.showerror("Error", "Not enough stock available.")
        else:
            messagebox.showerror("Error", "Invalid Product ID.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for Product ID and Quantity.")

# Create the main window for login
login_root = tk.Tk()
login_root.title("Inventory Management System")

# Create Username Label and Entry
tk.Label(login_root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(login_root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

# Create Password Label and Entry
tk.Label(login_root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(login_root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Create Login Button
tk.Button(login_root, text="Login", command=authenticate).grid(row=2, column=0, columnspan=2, pady=10)

# Start the Tkinter loop
login_root.mainloop()
