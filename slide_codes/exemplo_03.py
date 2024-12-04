from sqlalchemy import create_engine, text

# Cria a engine de conexão com o banco de dados PostgreSQL
engine = create_engine('postgresql+psycopg2://lazah:lazevedo@localhost:5432/exemplo_sqlalchemy', echo=True)

# Estabelece a conexão com o banco
connection = engine.connect()

# Definindo a consulta SQL completa
sql = text('SELECT id, name, comments FROM my_table')

# Executando a consulta
result = connection.execute(sql)

# Iterando sobre o resultado e imprimindo os registros
for row in result:
    print(row)

# Fechando a conexão
connection.close()
