from app import App
import os

# Clear terminal

'''My Calculator Test'''

if __name__ == '__main__':
    
    '''Using os.system(cls,clear) to give the user a fresh screen'''
    os.system('cls') # Windows
    os.system('clear') #Linux/MacOS
    
    print("Welcome To My Calculator App!")
    print("----------------------------------\n")
    app = App().start()