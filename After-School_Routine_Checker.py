from tkinter import *
from tkinter import messagebox

# Create the main window
root = Tk()
root.title("After-School Routine Checker")
root.geometry("450x300")

# Routine tasks
routine = [
    "Do Homework",
    "Have a Snack",
    "Play Outside",
    "Read a Book",
    "Go to Bed"
]

task_index = 0

# -----------------------------
# Function: Show last character
# -----------------------------
def show_last_character(event):
    text = entry.get()
    if text:
        result_label.config(text=f"Last character typed: {text[-1]}")
    else:
        result_label.config(text="Type a task...")

# -----------------------------
# Function: Mouse click event
# -----------------------------
def routine_clicked(event):
    result_label.config(text="Routine area clicked!")

# -----------------------------
# Function: Show next task
# -----------------------------
def next_task():
    global task_index

    if entry.get().strip() == "":
        messagebox.showwarning("Warning", "Please enter a task first!")
        return

    result_label.config(text=f"Next Task: {routine[task_index]}")
    task_index = (task_index + 1) % len(routine)

# Title
title = Label(root, text="After-School Routine Checker",
              font=("Arial", 16, "bold"))
title.pack(pady=10)

# Task Entry
entry = Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)

# Detect key release
entry.bind("<KeyRelease>", show_last_character)

# Clickable routine area
routine_frame = Frame(root, bg="lightblue", width=300, height=60)
routine_frame.pack(pady=10)
routine_frame.pack_propagate(False)

routine_label = Label(routine_frame,
                      text="Click Here (Routine Area)",
                      bg="lightblue",
                      font=("Arial", 12))
routine_label.pack(expand=True)

routine_frame.bind("<Button-1>", routine_clicked)
routine_label.bind("<Button-1>", routine_clicked)

# Button
button = Button(root, text="Show Next Task",
                command=next_task,
                font=("Arial", 12))
button.pack(pady=10)

# Output Label
result_label = Label(root, text="",
                     font=("Arial", 12),
                     fg="blue")
result_label.pack(pady=10)

# Run the application
root.mainloop()