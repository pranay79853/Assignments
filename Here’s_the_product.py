from tkinter import *

# Create the main window
root = Tk()
root.title("Product Calculator")
root.geometry("300x250")

# Function to calculate the product
def calculate_product():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    product = num1 * num2
    result_label.config(text="Product = " + str(product))

# Labels
Label(root, text="Enter First Number:").pack(pady=5)
entry1 = Entry(root)
entry1.pack()

Label(root, text="Enter Second Number:").pack(pady=5)
entry2 = Entry(root)
entry2.pack()

# Button
Button(root, text="Calculate Product", command=calculate_product).pack(pady=10)

# Result Label
result_label = Label(root, text="Product = ")
result_label.pack(pady=10)

# Run the application
root.mainloop()