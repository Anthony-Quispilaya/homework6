from app.commands import Command
from calculator.arithmetic_operations import divide
import os
class DivideCommand(Command):
    def execute(self):
        '''Using os.system(cls,clear) to give the user a fresh screen'''
        os.system('cls') # Windows
        os.system('clear') #Linux/MacOS
        # User enters two number, (automatically float type)
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            
            # Check for division by zero
            if b == 0:
                print("Error: Division by zero is not allowed.")
                return
            
            result = divide(a, b)
            print(f"The result of {a} / {b} = {result}")

        # Error if user does not enter float type
        except ValueError:
            print("Please enter valid numbers.")