
'''
Este exemplo cria um engine para se conectar a um banco de 
dados SQLite chamado `database.db`. 

Explicação:
1. **`create_engine`**: Importado do SQLAlchemy, é usado 
para criar um objeto engine, que gerencia a conexão com 
o banco de dados.
2. **`sqlite:///database.db`**: Especifica o banco de dados 
SQLite a ser utilizado. O prefixo `sqlite:///` indica um banco 
de dados local. Se o arquivo `database.db` não existir, ele 
será criado automaticamente.
3. **`print(engine)`**: Exibe informações sobre o objeto 
engine criado.

Este código prepara o ambiente para executar consultas 
SQL posteriormente.
'''

from sqlalchemy import create_engine


engine = create_engine('sqlite:///database.db')

print(engine)

'''
A saída:

    Engine(sqlite:///database.db)

indica que o objeto `engine` foi criado com sucesso para 
o banco de dados especificado.

- O SQLAlchemy representa o engine com o prefixo do banco 
de dados utilizado (`sqlite`) e a localização do 
arquivo (`database.db`).
- Esta é uma confirmação visual de que o motor de 
conexão está pronto para ser usado, mas nenhuma 
operação no banco de dados foi realizada ainda.
'''