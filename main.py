"""
Carolina Carrilho
May 2021
"""

import projectLib
from Bucket import Bucket
from Product import Product


bucket = Bucket() #class bucket

command = input("Insert your command: \n"
                "1. Regist your product \n"
                "2. See your products registred. \n"  
                "3. Amount to paid\n")


while command != 'exit':
    if command == '1':
        projectLib.add_register_prod(bucket)

    elif command == '2':
        projectLib.print_list_prod(bucket)

    #elif command == '3':
    #TODO: apresentar o calculo do subtot, desconto, e total(c/ desconto aplicado)


    else:
        print("Unknown command. Type help to see available commands.")

    command = input("")

print('Bye!')