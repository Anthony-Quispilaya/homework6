from app.commands import Command
import os
import logging
class MenuCommand(Command):
    def execute(self):
        '''Using os.system(cls,clear) to give the user a fresh screen'''
        os.system('cls') # Windows
        os.system('clear') #Linux/MacOS
        logging.info("Menu listed.")
        
        print("Type 'add' to add")
        print("Type 'subtract' to subtract")
        print("Type 'multiply' to multiply")
        print("Type 'divide' to divide")