# Conexão do Python com o MySQL

!["Imagem Python com MySQL"](https://miro.medium.com/v2/resize:fit:1137/1*OnDVcS17HTWZ2L2vPaaQ1A.png)

## Drive de comunicação com mysql
Para estabelecer a comunicação entre Python e
dados mysql, iremos usar o seguinte drive:
<a href="https://pypi.org/project/mysql-connector-python/#description"> https://pypi.org/project/mysql-connector-python/#description</a>

### Comando para instalar o drive
```python
    python -m pip install mysql-connector-python
```

### Configuração do banco de dados MySQL
O nosso banco de dados esta em um container de docker. Para
acessá-lo será necessário criar o container, então faremos
os seguintes comandos em um servidor Fedora com o docker
instalado:

#### Criação do volume
```shel
mkdir dadosclientes
```
#### Criação do container
<center>
<img src="image-1.png" "100" height "100">
</center>

```shel
docker run --name srv-mysql -v ~/dadosclientes:/var/lib/mysql -p 3784:3306 -e MYSQL_ROOT_PASSWORD=senac@123 -d mysql
```

### Criação do banco de dados e da tabela clientes

```
CREATE DATABASE banco;
USE banco;
CREATE TABLE clientes(
clientes_id int auto_increment primary key,
nome_cliente varchar(50) not null,
email varchar(100) not null unique,
telefone varchar(20)
)
```
 
 
```Python
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
    password="SENAC@123",
    database="banco"
)    
 # Estamos c
print(conexao)
 
#para se movimentar dentro da estrutura de
# banco de dados e retornar dos dados necessário
# iremos criar um cursor
cursor = conexao.cursor()
 
# Vamos executar um comando usando  o cursor
cursor.execute("Create database Ola")
 
# vamos executar um comando usando o cursor
# cursor.execute("Create database Ola")
 
# Vamos selecionar todos os bancos de dados na tabela cliente
cursor.execute("Insert into clientes(nome_cliente,email,telefone)values('Amanda','amanda@oul.com.br','(11)95487-6512')")
print(cursor)
for c in cursor:
    print(f"Id do cliente: {c [0]}")
    print(f"Nome do cliente: {c [1]}")
    print(f"Email: {c [2]}")
 
```

```Python
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
    password="SENAC@123",
    database="banco"
)    
 # Estamos c
print(conexao)
 
#para se movimentar dentro da estrutura de
# banco de dados e retornar dos dados necessário
# iremos criar um cursor
cursor = conexao.cursor()
 
# Vamos executar um comando usando  o cursor
cursor.execute("Create database Ola")
 
# vamos executar um comando usando o cursor
# cursor.execute("Create database Ola")
 
# Vamos selecionar todos os bancos de dados na tabela cliente
cursor.execute("Insert into clientes(nome_cliente,email,telefone)values('Amanda','amanda@oul.com.br','(11)95487-6512')")
print(cursor)
for c in cursor:
    print(f"Id do cliente: {c [0]}")
    print(f"Nome do cliente: {c [1]}")
    print(f"Email: {c [2]}")
 
```
### Arquivo de atualização: up_clientes.py

```python
import mysql.connector as mc
cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)

cursor = cx.cursor()
cursor.execute("Select * from clientes")
for i in cursor:
    print (i)

print("O que voce deseja atualizar, digite:")
print("1 - para Nome")
print("2 - para E-mail")
print("3 - parta Telefone")
op = input("Digite aopção desejada:")
id = input("Agora digite o id do cliente:")
dado = input("Digite a nova informação: ")
if(op=="1"):
    cursor.execute("update clientes set nome_cliente='"+dado+"'where clientes_id="+id)
elif(op=="2"):
    cursor.execute("update clientes set email='"+dado+"'where clientes_id="+id)
elif(op=="3"):
    cursor.execute("update clientes set telefone='"+dado+"'where clientes_id="+id)
else:
    print("Opção inválida!")

cx.commit()