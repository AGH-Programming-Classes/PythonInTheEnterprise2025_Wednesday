import tkinter as tk
import re


class CalculatorFabrica:
   def createCalc(self, type: str):
      types = {"normal": NormiesCalc, "business": BusinessCalc}
      if type not in types.keys():
         raise ValueError
      return types[type]()


class NormiesCalc:
   def __init__(self):
      self.root = tk.Tk()
      self.root.title("Kalkulator")
      self.root.geometry("450x600")
      self.root.resizable(False, False)
   
      self.entry = tk.Entry(self.root, width=16, font=('Arial', 24), bd=5, relief=tk.RIDGE, justify='right')
      self.entry.grid(row=0, column=0, columnspan=4, pady=10)
   
      self.buttons = [
          '7', '8', '9', '/',
          '4', '5', '6', '*',
          '1', '2', '3', '-',
          '0', '.', '=', '+'
      ]

   def click(self, button_text):
      current = self.entry.get()
      self.entry.delete(0, tk.END)
      self.entry.insert(0, current + button_text)

   def clear(self):
      self.entry.delete(0, tk.END)

   def calculate(self):
      if re.fullmatch(r"[0-9+\-*/(). ]+", self.entry.get()):
         try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
         except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Błąd")

   def calc_main(self):
   
      row = 1
      col = 0
   
      for button in self.buttons:
          if button == '=':
              b = tk.Button(self.root, text=button, width=5, height=2, font=('Arial', 18),
                            command=self.calculate)
          else:
              b = tk.Button(self.root, text=button, width=5, height=2, font=('Arial', 18),
                            command=lambda txt=button: self.click(txt))
   
          b.grid(row=row, column=col, padx=5, pady=5)
          col += 1
          if col > 3:
              col = 0
              row += 1
   
      clear_btn = tk.Button(self.root, text='C', width=22, height=2, font=('Arial', 18), command=self.clear)
      clear_btn.grid(row=6, column=0, columnspan=4, padx=5, pady=10)
   
      self.root.mainloop()

class BusinessCalc:
   def __init__(self):
      self.root = tk.Tk()
      self.root.title("Kalkulator")
      self.root.geometry("450x600")
      self.root.resizable(False, False)
      self.root.configure(bg='green')
   
      self.entry = tk.Entry(self.root, width=16, font=('Arial', 24), bd=5, relief=tk.RIDGE, justify='right')
      self.entry.grid(row=0, column=0, columnspan=4, pady=10)
   
      self.buttons = [
          '7', '8', '9', '/',
          '4', '5', '6', '*',
          '1', '2', '3', '-',
          '0', '.', '=', '+'
      ]

   def click(self, button_text):
      current = self.entry.get()
      self.entry.delete(0, tk.END)
      self.entry.insert(0, current + button_text)

   def clear(self):
      self.entry.delete(0, tk.END)

   def calculate(self):
      if re.fullmatch(r"[0-9+\-*/(). ]+", self.entry.get()):
         try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
         except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Błąd")

   def calc_main(self):
   
      row = 1
      col = 0
   
      for button in self.buttons:
          if button == '=':
              b = tk.Button(self.root, text=button, width=5, height=2, font=('Arial', 18),
                            command=self.calculate)
          else:
              b = tk.Button(self.root, text=button, width=5, height=2, font=('Arial', 18),
                            command=lambda txt=button: self.click(txt))
   
          b.grid(row=row, column=col, padx=5, pady=5)
          col += 1
          if col > 3:
              col = 0
              row += 1
   
      clear_btn = tk.Button(self.root, text='C', width=22, height=2, font=('Arial', 18), command=self.clear)
      clear_btn.grid(row=6, column=0, columnspan=4, padx=5, pady=10)
   
      self.root.mainloop()