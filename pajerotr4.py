import sqlite3
from tkinter import *

# Função para executar a consulta no banco de dados
def consultar_peca():
    # Conectar ao banco de dados
    conn = sqlite3.connect('exemplo.db')
    cursor = conn.cursor()

    # Executar a consulta SQL
    cursor.execute("SELECT * FROM mitsubishi")

    # Obter os resultados da consulta
    resultados = cursor.fetchall()

    # Exibir os resultados na interface
    for resultado in resultados:
        print(resultado)

    # Fechar a conexão com o banco de dados
    cursor.close()
    conn.close()

# Criar a interface gráfica
root = Tk()
root.title("Consulta de Peças")

# Botão para consultar as peças
btn_consultar = Button(root, text="Consultar Peças", command=consultar_peca)
btn_consultar.pack(pady=10)

# Executar a interface gráfica
root.mainloop()
