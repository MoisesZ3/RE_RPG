import sqlite3
from personagem_save import Save

if __name__ == '__main__':
    Save.criar_tabela_herois()
    Save.criar_tabela_saves()
    Save.criar_tabela_inventario()