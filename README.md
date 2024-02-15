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
