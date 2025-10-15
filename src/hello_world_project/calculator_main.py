def calculator_main():
    running = True
    calculation = -1
    while running:
         calculation = input("-1 for exit\n")
         if calculation == "-1":
            running = False
            break
         print(eval(calculation))
