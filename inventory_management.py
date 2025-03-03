import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to create the database and table
def create_database():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  quantity INTEGER NOT NULL,
                  price REAL NOT NULL)''')
    conn.commit()
    conn.close()

# Function to add a product
def add_product():
    name = entry_name.get()
    quantity = entry_quantity.get()
    price = entry_price.get()

    if name and quantity and price:
        try:
            quantity = int(quantity)
            price = float(price)
            conn = sqlite3.connect('inventory.db')
            c = conn.cursor()
            c.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)",
                      (name, quantity, price))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Product added successfully!")
            view_products()
        except ValueError:
            messagebox.showerror("Error", "Quantity must be an integer and price must be a number.")
    else:
        messagebox.showerror("Error", "All fields are required.")

# Function to view all products
def view_products():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    rows = c.fetchall()
    conn.close()

    listbox_products.delete(0, tk.END)
    for row in rows:
        listbox_products.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Quantity: {row[2]}, Price: {row[3]}")

# Function to delete a product
def delete_product():
    selected_product = listbox_products.get(tk.ACTIVE)
    if selected_product:
        product_id = selected_product.split(",")[0].split(":")[1].strip()
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        c.execute("DELETE FROM products WHERE id=?", (product_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Product deleted successfully!")
        view_products()
    else:
        messagebox.showerror("Error", "No product selected.")

# Function to generate low-stock alert
def low_stock_alert():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE quantity < 10")
    rows = c.fetchall()
    conn.close()

    if rows:
        alert_message = "Low stock alert for the following products:\n"
        for row in rows:
            alert_message += f"ID: {row[0]}, Name: {row[1]}, Quantity: {row[2]}\n"
        messagebox.showwarning("Low Stock Alert", alert_message)
    else:
        messagebox.showinfo("Info", "No products with low stock.")

# Create the main window
root = tk.Tk()
root.title("Inventory Management System")

# Create and place the widgets
label_name = tk.Label(root, text="Product Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_quantity = tk.Label(root, text="Quantity:")
label_quantity.grid(row=1, column=0, padx=10, pady=10)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row=1, column=1, padx=10, pady=10)

label_price = tk.Label(root, text="Price:")
label_price.grid(row=2, column=0, padx=10, pady=10)
entry_price = tk.Entry(root)
entry_price.grid(row=2, column=1, padx=10, pady=10)

button_add = tk.Button(root, text="Add Product", command=add_product)
button_add.grid(row=3, column=0, columnspan=2, pady=10)

listbox_products = tk.Listbox(root, width=50)
listbox_products.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

button_delete = tk.Button(root, text="Delete Product", command=delete_product)
button_delete.grid(row=5, column=0, pady=10)

button_low_stock = tk.Button(root, text="Low Stock Alert", command=low_stock_alert)
button_low_stock.grid(row=5, column=1, pady=10)

# Create the database and table if they don't exist
create_database()

# View products on startup
view_products()

# Start the main loop
root.mainloop()