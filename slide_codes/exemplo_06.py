from sqlalchemy import create_engine, text

engine = create_engine('postgresql+psycopg2://lazah:lazevedo@localhost:5432/exemplo_sqlalchemy', echo=True)

query = 'SELECT id, name, comments FROM my_table limit 10 offset {of}'

with engine.connect() as connection:
    with connection.begin():
        sql = text(query.format(of=0))
        result1 = connection.execute(sql)
        for row in result1:
            print(row)
    with connection.begin():
        sql = text(query.format(of=1))
        result2 = connection.execute(sql)
        for row in result2:
            print(row)
    with connection.begin():
        sql = text(query.format(of=2))
        result3 = connection.execute(sql)
        for row in result3:
            print(row)
