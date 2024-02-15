# Importando a a biblioteca de conexão com o banco 
# de dados mysql
 
# Vamos adicionar um alias a biblioteca
 
import mysql.connector as mc
 
# Vamos estabelecer a conexao com o banco 
# de dados e para tal, iremos passar os seguintes dados:
# servidor, porta, usuário, senha, banco 
 
conexao = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)    
# Estamos testando a conexão, pedindo para 
# exibir o id da conexão. Caso exiba uma
# pilha de erros, então você tem um erro
# na linha de conexão

print(conexao)

# para se movimentar dentro da estrutura de
# banco de dados e retornar dos dados necessarios
# iremos criar um cursor
cursor = conexao.cursor()

# Vamos executar um comando usando o cursor
# cunsor.execute("Create database Ola")

# Vamos selecionar todos os dados da tabela cliente
cursor.execute("Insert into clientes(nome_cliente,email,telefone)values('Amanda', 'amanda@oul.com.br','(11)95487-6512')")
print(cursor)
for c in cursor:
    print(c)
    print(f"Id do cliente: {c[0]}")
    print(f"Nome do cliente: {c[1]}")
    print(f"Email: {c[2]}")
 