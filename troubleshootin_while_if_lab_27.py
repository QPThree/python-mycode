# Lab 27

#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.
calc1 = 0.0
calc2 = 0.0
operation = ""
while (calc1 != "q"):
    calc1 = input("\nWhat is the first operator? Or, enter q to quit: ")
    if calc1.lower() == "q":
        break
    try:
        calc1=float(calc1)
    except:
        print("Not an integer")
        continue        
    calc2 = input("\nWhat is the second operator? Or, enter q to quit: ")
    if calc2.lower() == "q":
        break
    try:
        calc2=float(calc2)
    except:
        print("Not an integer")
        continue 
    operation = input("Enter an operation to perform on the two operators (+ or -): ")
    if operation == "+":
        print(f"\n {str(calc1)} + {str(calc2)} = {str(calc1 + calc2)}")
    elif operation == '-':
        print(f"\n {str(calc1)} - {str(calc2)} = {str(calc1 - calc2)}")
    else:
        print("\n Not a valid entry. Restarting...")
