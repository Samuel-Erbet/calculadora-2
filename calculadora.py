from os import system
from formulas import * 

system('clear')

print('''
____ ____ _    ____ _  _ _    ____ ___  ____ ____ ____ 
|    |__| |    |    |  | |    |__| |  \ |  | |__/ |__| 
|___ |  | |___ |___ |__| |___ |  | |__/ |__| |  \ |  |                                                    

 _____________________
|  _________________  |
| |    calculadora  | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | * | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |   
|_____________________|

''')

while True:
    conta = input('[conta]==-> ')
    print(eval(conta))