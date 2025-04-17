import sqlite3
import time
from colorama import *

with sqlite3.connect("management.db") as db:
    adm = db.cursor()

    adm.execute("""

    CREATE TABLE IF NOT EXISTS produtos (
        nome text,
        preco REAL,
        id INTEGER
    )

    """)


    def add_product(productName, productPrice, productId):
        with sqlite3.connect("management.db") as db:
            adm = db.cursor()
            adm.execute(f"SELECT * FROM produtos WHERE id = {productId}")
            resultado = adm.fetchone()
            if resultado:
                print(f"{Back.RED}[!]{Style.RESET_ALL} Já existe um produto com com esse id!")
                time.sleep(3)
            else:
                adm.execute("INSERT INTO produtos (nome, preco, id) VALUES (?, ?, ?)", (str(productName), float(productPrice), int(productId)))
                print(f"{Back.GREEN}[!]{Style.RESET_ALL} Produto cadastrado com sucesso!")
                time.sleep(3)
            
        db.commit()

    def remove_product():
        with sqlite3.connect("management.db") as db:
            adm = db.cursor()
            productIdD = input("Id do produto que queres apagar: ")
            adm.execute("DELETE FROM produtos WHERE id = ?", (productIdD,))
            print(f"{Back.GREEN}[!]{Style.RESET_ALL} Produto apagado com sucesso.")
            time.sleep(3)

    def change_price():
        with sqlite3.connect("management.db") as db:
            adm = db.cursor()
            productIdP = int(input("Id do produto que queres mudar o preço: "))
            newPrice = float(input("Novo preço: "))
            adm.execute("UPDATE produtos SET preco = ? WHERE id = ?", (newPrice, productIdP))
            adm.execute("SELECT * FROM produtos WHERE preco = ?", (newPrice,))
            res = adm.fetchone()
            if res:
                print(f"{Back.GREEN}[!]{Style.RESET_ALL} Preco alterado com sucesso.")
            else:
                print(f"{Back.RED}[!]{Style.RESET_ALL} Não foi possível alterar o preco do produto.")
            time.sleep(3)

