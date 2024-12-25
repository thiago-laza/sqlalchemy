from sqlalchemy import create_engine, inspect

# Configuração da engine para conectar ao banco de dados
engine = create_engine('postgresql+psycopg2://postgres:lazevedo@localhost:5432/exemplo_sqlalchemy')

# Inspecionar o banco de dados
inspected = inspect(engine)

# Obter as tabelas no banco de dados
tables = inspected.get_table_names()
print("Tabelas no banco de dados:", tables)

# Obter as colunas da tabela 'comments'
columns = inspected.get_columns('comments')
print("\nColunas da tabela 'comments':")
for column in columns:
    print(f"Nome: {column['name']}, Tipo: {column['type']}")




'''
- O código cria uma engine para se conectar ao banco de 
dados e utiliza o módulo 'inspect' para obter informações 
sobre as tabelas e colunas do banco de dados.

-  A função 'get_table_names()' retorna uma lista com os 
nomes das tabelas no banco de dados.

- A função 'get_columns()' retorna informações sobre as 
colunas de uma tabela específica, no caso, da tabela 'comments'.
'''


