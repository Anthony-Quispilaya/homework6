from app.commands import Command
from calculator.arithmetic_operations import subtract
import os
import logging
class SubtractCommand(Command):
    def execute(self):
        '''Using os.system(cls,clear) to give the user a fresh screen'''
        os.system('cls') # Windows
        os.system('clear') #Linux/MacOS
        logging.info("Subtraction operation started.")
        
        
        # User enters two number, (automatically float type)
        while True:
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                result = subtract(a, b)
        
                logging.info(f"The result of {a} - {b} = {result}")
                break
            
            # Error if user does not enter float type
            except ValueError:
                logging.warning("Please enter valid numbers.")