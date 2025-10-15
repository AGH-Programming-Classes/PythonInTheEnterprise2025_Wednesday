from utils import *
from example_module import *
from tkinter import *

def main():
    master = Tk()
    calc = Calculator(master)
    master.mainloop()

if __name__ == "__main__":
    main()
