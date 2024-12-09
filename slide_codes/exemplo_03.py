from sqlalchemy import create_engine, text

engine = create_engine('postgresql+psycopg2://lazah:lazevedo@localhost:5432/exemplo_sqlalchemy', echo=True)

connection = engine.connect()

sql = text('SELECT id, name, comments FROM my_table')

result = connection.execute(sql)

for row in result:
    print(row)

connection.close()