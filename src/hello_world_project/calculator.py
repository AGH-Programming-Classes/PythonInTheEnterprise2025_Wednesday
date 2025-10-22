import tkinter as tk
from tkinter import messagebox
import math
from utils import safe_eval, is_operator
from example_module import log_calculation

class Calculator:
  def __init__(self, master):
    self.master = master
    master.title("Calculator")
    master.geometry("320x480")
    master.resizable(True, True)
    master.configure(bg="#2c2c2c")

    self.expression = ""
    self.input_text = tk.StringVar()

    self.create_widgets()
    self.bind_keys()
  def create_widgets(self):
    input_frame = tk.Frame(self.master, bd=0, bg="#2c2c2c")
    input_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    self.input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'),
                                textvariable=self.input_text,
                                bg="#4a4a4a", fg="white", bd=0,
                                justify=tk.RIGHT, insertbackground="white")
    self.input_field.pack(expand=True, fill=tk.BOTH, ipady=10)

    btns_frame = tk.Frame(self.master, bg="#2c2c2c")
    btns_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Buttons
    self.create_button(btns_frame, "(", 1, 0, command=lambda: self.button_click('('))
    self.create_button(btns_frame, ")", 1, 1, command=lambda: self.button_click(')'))
    self.create_button(btns_frame, "C", 1, 2, bg="#d9534f", command=self.clear_all)
    self.create_button(btns_frame, "←", 1, 3, command=self.clear_last)

    self.create_button(btns_frame, "/", 2, 0, command=lambda: self.button_click('/'))
    self.create_button(btns_frame, "*", 2, 1, command=lambda: self.button_click('*'))
    self.create_button(btns_frame, "^", 2, 2, command=lambda: self.button_click('**'))
    self.create_button(btns_frame, "√", 2, 3, command=self.sqrt_operation)

    self.create_button(btns_frame, "7", 3, 0, command=lambda: self.button_click('7'))
    self.create_button(btns_frame, "8", 3, 1, command=lambda: self.button_click('8'))
    self.create_button(btns_frame, "9", 3, 2, command=lambda: self.button_click('9'))
    self.create_button(btns_frame, "-", 3, 3, command=lambda: self.button_click('-'))

    self.create_button(btns_frame, "4", 4, 0, command=lambda: self.button_click('4'))
    self.create_button(btns_frame, "5", 4, 1, command=lambda: self.button_click('5'))
    self.create_button(btns_frame, "6", 4, 2, command=lambda: self.button_click('6'))
    self.create_button(btns_frame, "+", 4, 3, command=lambda: self.button_click('+'))

    self.create_button(btns_frame, "1", 5, 0, command=lambda: self.button_click('1'))
    self.create_button(btns_frame, "2", 5, 1, command=lambda: self.button_click('2'))
    self.create_button(btns_frame, "3", 5, 2, command=lambda: self.button_click('3'))
    self.create_button(btns_frame, "=", 5, 3, rowspan=2, bg="#007bff", command=self.calculate)

    self.create_button(btns_frame, "0", 6, 0, columnspan=2, command=lambda: self.button_click('0'))
    self.create_button(btns_frame, ".", 6, 2, command=lambda: self.button_click('.'))

    for i in range(4):
        btns_frame.grid_columnconfigure(i, weight=1)
    for i in range(1, 7):
        btns_frame.grid_rowconfigure(i, weight=1)
  
  def create_button(self, parent_frame, text, row, column, columnspan=1, rowspan=1, bg="#4a4a4a", fg="white", command=None):
    button = tk.Button(parent_frame, text=text, font=('arial', 15, 'bold'),
                       bd=0, bg=bg, fg=fg, width=6, height=2,
                       command=command,
                       activebackground="#6a6a6a", activeforeground="white")
    button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, padx=1, pady=1, sticky="nsew")

  def bind_keys(self):
    for key in "0123456789+-*/().":
        self.master.bind(key, self.keyboard_click)
    self.master.bind("<Shift-6>", lambda event=None: self.button_click('**'))
    self.master.bind("<Return>", lambda event=None: self.calculate())
    self.master.bind("<BackSpace>", lambda event=None: self.clear_last())
    self.master.bind("<Delete>", lambda event=None: self.clear_all())
  
  def keyboard_click(self, event):
    if event.char in "0123456789+-*/()."
    self.button_click(event.char)
    
  def button_click(self, item):
    if not self.expression and is_operator(item) and item != '-':
        return
    if self.expression and is_operator(self.expression[-1]) and is_operator(item):
        self.expression = self.expression[:-1]
    self.expression += str(item)
    self.input_text.set(self.expression)
    self.input_field.xview_moveto(1)

  def sqrt_operation(self):
    try:
        if not self.expression:
            return
        value_to_sqrt = safe_eval(self.expression)
        if value_to_sqrt < 0:
            messagebox.showerror("Error", "Cannot take square root of a negative number!")
            return
        result = str(math.sqrt(value_to_sqrt))
        self.input_text.set(result)
        self.expression = result
    except Exception as e:
        messagebox.showerror("Error", f"Invalid operation: {e}")
        self.clear_all()

  def clear_all(self):
      self.expression = ""
      self.input_text.set("")

  def clear_last(self):
      self.expression = self.expression[:-1]
      self.input_text.set(self.expression)

  def calculate(self):
      try:
          if not self.expression:
              self.input_text.set("0")
              return
          result = str(safe_eval(self.expression))
          self.input_text.set(result)
          self.expression = result
          log_calculation(self.expression, result)
      except Exception as e:
          messagebox.showerror("Error", f"Invalid expression: {e}")
          self.clear_all()
