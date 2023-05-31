import psycopg2
from tkinter import *

# Função para executar a consulta no banco de dados PostgreSQL
def consultar_peca_postgresql():
    carro = entry_carro.get()  # Obter o valor digitado pelo usuário

    conn = None
    cursor = None
    try:
        # Conectar ao banco de dados PostgreSQL
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="246895"
        )
        cursor = conn.cursor()

        # Executar a consulta SQL no PostgreSQL usando o valor do carro
        cursor.execute(f"SELECT * FROM mitsubishi WHERE carro = '{carro}'")

        # Obter os resultados da consulta
        resultados = cursor.fetchall()

        # Criar uma nova janela para exibir os resultados
        result_window = Toplevel(root)
        result_window.title("Resultados da Consulta")

        # Área de texto para exibir os resultados
        result_text = Text(result_window)
        result_text.pack()

        # Exibir os resultados na área de texto
        for resultado in resultados:
            result_text.insert(END, str(resultado) + "\n")

    except psycopg2.Error as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")

    finally:
        # Fechar o cursor e a conexão com o banco de dados PostgreSQL
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

# Criar a interface gráfica
root = Tk()
root.title("Consulta de Peças")

# Entrada de texto para digitar o carro
entry_carro = Entry(root)
entry_carro.pack(pady=10)

# Botão para consultar as peças no PostgreSQL
btn_consultar_postgresql = Button(root, text="Consultar Peças (PostgreSQL)", command=consultar_peca_postgresql)
btn_consultar_postgresql.pack(pady=10)

# Executar a interface gráfica
root.mainloop()
