import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        # 1. Retrieve integers from the entry fields
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        
        # 2. Validate and create date objects
        birth_date = date(year, month, day)
        today = date.today()
        
        if birth_date > today:
            messagebox.showerror("Error", "Birth date cannot be in the future!")
            return
            
        # 3. Calculate age breakdown
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day
        
        # Adjust for negative days
        if days < 0:
            # Move back one month
            months -= 1
            # Find previous month length to borrow days correctly
            if today.month == 1:
                prev_month = 12
                prev_year = today.year - 1
            else:
                prev_month = today.month - 1
                prev_year = today.year
                
            # Number of days in the birth month or current month context
            days_in_prev_month = (date(prev_year, prev_month + 1, 1) - date(prev_year, prev_month, 1)).days if prev_month < 12 else 31
            days += days_in_prev_month
            
        # Adjust for negative months
        if months < 0:
            years -= 1
            months += 12
            
        # 4. Display the result
        result_text = f"Age: {years} Years, {months} Months, {days} Days"
        label_result.config(text=result_text, fg="green")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers for Day, Month, and Year.")

# --- UI Setup ---
root = tk.Tk()
root.title("Age Calculator")
root.geometry("350x250")
root.resizable(False, False)

# Labels and Entries
tk.Label(root, text="Day (DD):", font=("Arial", 10)).pack(pady=2)
entry_day = tk.Entry(root, width=15)
entry_day.pack()

tk.Label(root, text="Month (MM):", font=("Arial", 10)).pack(pady=2)
entry_month = tk.Entry(root, width=15)
entry_month.pack()

tk.Label(root, text="Year (YYYY):", font=("Arial", 10)).pack(pady=2)
entry_year = tk.Entry(root, width=15)
entry_year.pack()

# Calculate Button
btn_calculate = tk.Button(root, text="Calculate Age", command=calculate_age, bg="blue", fg="white", font=("Arial", 10, "bold"))
btn_calculate.pack(pady=15)

# Result Display Label
label_result = tk.Label(root, text="", font=("Arial", 12, "bold"))
label_result.pack()

# Run the app
root.mainloop()
