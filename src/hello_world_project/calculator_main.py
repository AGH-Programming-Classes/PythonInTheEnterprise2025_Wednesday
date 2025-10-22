import tkinter as tk
import re

def click(button_text):
   current = entry.get()
   entry.delete(0, tk.END)
   entry.insert(0, current + button_text)

def clear():
   entry.delete(0, tk.END)

def calculate():
   if re.fullmatch(r"[0-9+\-*/(). ]+", entry.get()):
      try:
         result = eval(entry.get())
         entry.delete(0, tk.END)
         entry.insert(0, str(result))
      except:
         entry.delete(0, tk.END)
         entry.insert(0, "Błąd")

root = tk.Tk()
root.title("Kalkulator")
root.geometry("450x600")
root.resizable(False, False)
root.configure(bg='green')

entry = tk.Entry(root, width=16, font=('Arial', 24), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        b = tk.Button(root, text=button, width=5, height=2, font=('Arial', 18),
                      command=calculate)
    else:
        b = tk.Button(root, text=button, width=5, height=2, font=('Arial', 18),
                      command=lambda txt=button: click(txt))
    
    b.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

clear_btn = tk.Button(root, text='C', width=22, height=2, font=('Arial', 18), command=clear)
clear_btn.grid(row=6, column=0, columnspan=4, padx=5, pady=10)

root.mainloop()
