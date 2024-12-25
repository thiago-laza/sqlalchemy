from sqlalchemy import MetaData, Table, create_engine

engine = create_engine('postgresql+psycopg2://postgres:lazevedo@localhost:5432/exemplo_sqlalchemy')

metadata = MetaData()

comments = Table('comments', metadata, autoload_with=engine)

print(comments.c)
print(comments.columns)
print(comments.c.id)

'''

- O código cria uma engine para se conectar ao banco de dados 
e usa o objeto 'MetaData' para gerenciar informações de 
esquemas de banco de dados.

- O objeto 'Table' é usado para representar a tabela 
'comments', que é carregada automaticamente com base 
no banco de dados, usando a engine.

- A função 'autoload_with' faz com que a tabela seja 
carregada diretamente do banco de dados.

- 'comments.c' fornece acesso às colunas da tabela como
 um atributo, e 'comments.columns' também retorna as 
 colunas, mas como um dicionário.

- 'comments.c.id' acessa diretamente a coluna 'id' 
da tabela 'comments'.

'''