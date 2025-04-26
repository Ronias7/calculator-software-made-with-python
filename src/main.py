import tkinter as tk
from tkinter import ttk
import os
from logic.logic import CalculatorLogic

def create_calculator():
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("410x610")  # Adjust window size slightly to account for the border

    # Set a light gray background for the entire window
    root.configure(bg="black")  # Black background for the border

    # Create a frame to hold the calculator content
    main_frame = tk.Frame(root, bg="#d3d3d3", bd=0)  # Light gray background for the calculator
    main_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)  # Add padding for the black border

    # Dynamically determine the path to the .ico file
    base_dir = os.path.dirname(__file__)  # Directory of the current file
    icon_path = os.path.join(base_dir, "assets", "cal_icon.ico")  # Path to the .ico file

    # Set the window icon
    if os.path.exists(icon_path):  # Check if the .ico file exists
        root.iconbitmap(icon_path)
    else:
        print(f"Warning: Icon file not found at {icon_path}")

    logic = CalculatorLogic()  # Create an instance of CalculatorLogic

    # Configure grid to expand dynamically
    main_frame.rowconfigure(0, weight=1)
    for i in range(5):  # 5 rows (1 for display, 4 for buttons)
        main_frame.rowconfigure(i, weight=1)
    for i in range(4):  # 4 columns
        main_frame.columnconfigure(i, weight=1)

    # Display
    display = tk.Entry(main_frame, font=("Arial", 30), justify="right", bd=10, bg="#f0f0f0")  # Increased font size to 30
    display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

    # Flag to track if an error occurred
    error_occurred = [False]

    # Button click handler
    def on_button_click(char):
        if error_occurred[0]:
            # Clear the display if an error occurred before appending new input
            display.delete(0, tk.END)
            error_occurred[0] = False

        if char == "C":
            display.delete(0, tk.END)  # Clear the display
        elif char == "=":
            expression = display.get()
            try:
                result = logic.evaluate(expression)  # Use the logic to evaluate the expression
                display.delete(0, tk.END)
                display.insert(tk.END, str(result))
            except ValueError:
                display.delete(0, tk.END)
                display.insert(tk.END, "Error")
                error_occurred[0] = True  # Set the error flag
        else:
            display.insert(tk.END, char)  # Append the character to the display

    # Style for buttons
    style = ttk.Style()
    style.configure("TButton",
                    font=("Arial", 18),
                    padding=10,
                    relief="flat",
                    background="#d9e4f5",
                    foreground="black")
    style.map("TButton",
              background=[("active", "#b0c4de")])  # Hover effect

    # Buttons
    buttons = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "C", "0", "=", "+"
    ]

    row_val = 1
    col_val = 0

    for button in buttons:
        btn = ttk.Button(
            main_frame, text=button, style="TButton", command=lambda b=button: on_button_click(b)
        )
        btn.grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    root.mainloop()

if __name__ == "__main__":
    create_calculator()