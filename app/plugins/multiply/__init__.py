from app.commands import Command
from calculator.arithmetic_operations import multiply
import os
class MultiplyCommand(Command):
    def execute(self):
        '''Using os.system(cls,clear) to give the user a fresh screen'''
        os.system('cls') # Windows
        os.system('clear') #Linux/MacOS
        
        # User enters two number, (automatically float type)
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            result = multiply(a, b)
    
            print(f"The result of {a} x {b} = {result}")
        
        # Error if user does not enter float type
        except ValueError:
            print("Please enter valid numbers.")