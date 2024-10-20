import sys
from app.commands import Command
import os
class ExitCommand(Command):
    def execute(self):
        '''Using os.system(cls,clear) to give the user a fresh screen'''
        os.system('cls') # Windows
        os.system('clear') #Linux/MacOS
        sys.exit("Exiting...")