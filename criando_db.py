import sqlite3

conectar = sqlite3.connect('cadastro.db')
c = conectar.cursor()

def criar_db():
    c.execute('CREATE TABLE cadastro (usuario text, senha text)')

try:
    criar_db()
except:
    print("Error ao criar o banco de dados")
else:
    print("banco de dados criado com sucesso!")














