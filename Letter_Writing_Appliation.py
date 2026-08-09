import tkinter as tk
from tkinter import filedialog

def open_letter():
    filename = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if filename:
        with open(filename, "r") as file:
            letter = file.read()

        text_editor.delete("1.0", tk.END)
        text_editor.insert("1.0", letter)

        window.title(filename)


def save_letter():
    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if filename:
        letter = text_editor.get("1.0", tk.END)

        with open(filename, "w") as file:
            file.write(letter)

        window.title(filename)


# Create the main window
window = tk.Tk()
window.title("Letter Writing Application")
window.geometry("700x500")

# Text editor
text_editor = tk.Text(window, width=80, height=25)
text_editor.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Buttons
open_button = tk.Button(
    window,
    text="Open Letter",
    command=open_letter
)
open_button.grid(row=1, column=0, padx=10, pady=10)

save_button = tk.Button(
    window,
    text="Save Letter",
    command=save_letter
)
save_button.grid(row=1, column=1, padx=10, pady=10)

# Start the application
window.mainloop()