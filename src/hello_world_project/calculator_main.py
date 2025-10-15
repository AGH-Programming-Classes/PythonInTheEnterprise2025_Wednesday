def calculator_main():
    ''' This function is responsible for the main loop of the program '''
    running = True
    calculation = -1
    while running:
         calculation = input("Choose calculation type 0 for addition 1 for subtraction other for exit")
         if calculation == 0:
            continue
         elif calculation == 1:
            continue
         else:
            running = False
