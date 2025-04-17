import time
import os
import sqlite3
import colorama
from colorama import *
from database import add_product
from database import remove_product
from database import change_price

while True:    
    os.system("cls" if os.name == "nt" else "clear")

    print(f"{Back.GREEN}Bem vindo ao sistema de administração mercadorial{Style.RESET_ALL}")

    print(f"{Back.GREEN}1]{Style.RESET_ALL} Adicionar produto")
    print(f"{Back.GREEN}2]{Style.RESET_ALL} Remover produto")
    print(f"{Back.GREEN}3]{Style.RESET_ALL} Mudar preço\n")


    chc = int(input("> "))

    try:
        if chc == 1:
            productName = str(input("Nome do produto: "))
            productPrice = float(input("Preco do produto: "))
            productId = int(input("Id do produto: "))
            database.add_product(productName, productPrice, productId)
        elif chc == 2:
            remove_product()
        elif chc == 3:
            change_price()

    except KeyboardInterrupt:
        exit()

    
    
