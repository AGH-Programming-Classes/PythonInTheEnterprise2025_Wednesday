import tkinter as tk
from calculator import Calculator, Observer

def main():
    root = tk.Tk()
    app = Calculator(root)
    button_obs = Observer()
    app.add_obs(button_obs)
    root.mainloop()

if __name__ == "__main__":
    main()
