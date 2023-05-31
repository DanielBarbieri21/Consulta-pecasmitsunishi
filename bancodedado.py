import psycopg2

# Conectar ao banco de dados
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="246895"
)

# Criar um cursor para executar as consultas SQL
cursor = conn.cursor()

# Executar uma consulta
cursor.execute("SELECT * FROM mitsubishi")

# Obter os resultados da consulta
resultados = cursor.fetchall()

# Exibir os resultados
for resultado in resultados:
    print(resultado)

# Fechar o cursor e a conexão com o banco de dados
cursor.close()
conn.close()
