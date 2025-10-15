import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator") # Window title
        master.geometry("320x450") # Increased height to accommodate parentheses and new operations
        master.resizable(False, False)
        master.configure(bg="#2c2c2c")

        self.expression = ""
        self.input_text = tk.StringVar()
