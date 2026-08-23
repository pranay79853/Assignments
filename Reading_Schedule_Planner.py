import tkinter as tk
from tkinter import messagebox

# Function to open the Reading Schedule Planner
def open_planner():
    planner = tk.Toplevel(root)
    planner.title("Reading Schedule Planner")
    planner.geometry("400x300")

    # Title
    tk.Label(
        planner,
        text="Reading Schedule Planner",
        font=("Arial", 16, "bold")
    ).pack(pady=15)

    # Total pages
    tk.Label(planner, text="Total number of pages:").pack()
    total_pages_entry = tk.Entry(planner)
    total_pages_entry.pack(pady=5)

    # Pages per day
    tk.Label(planner, text="Pages to read each day:").pack()
    pages_per_day_entry = tk.Entry(planner)
    pages_per_day_entry.pack(pady=5)

    # Result label
    result_label = tk.Label(planner, text="", font=("Arial", 11))
    result_label.pack(pady=15)

    # Calculate function
    def calculate_schedule():
        try:
            total_pages = int(total_pages_entry.get())
            pages_per_day = int(pages_per_day_entry.get())

            if total_pages <= 0 or pages_per_day <= 0:
                raise ValueError

            complete_days = total_pages // pages_per_day
            remaining_pages = total_pages % pages_per_day

            result_label.config(
                text=f"Complete reading days: {complete_days}\n"
                     f"Remaining pages: {remaining_pages}"
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter positive whole numbers."
            )

    # Calculate button
    tk.Button(
        planner,
        text="Calculate",
        command=calculate_schedule
    ).pack(pady=5)


# Main window
root = tk.Tk()
root.title("Reading Schedule Planner")
root.geometry("400x200")

tk.Label(
    root,
    text="Reading Schedule Planner",
    font=("Arial", 18, "bold")
).pack(pady=30)

tk.Label(
    root,
    text="Click the button below to plan your reading."
).pack(pady=5)

tk.Button(
    root,
    text="Open Planner",
    command=open_planner
).pack(pady=15)

# Start the program
root.mainloop()