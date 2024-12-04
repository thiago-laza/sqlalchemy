from sqlalchemy import create_engine

engine_pg = create_engine('postgresql+psycopg2://lazah:lazevedo@localhost:5432/exemplo_sqlalchemy')
print(engine_pg.dialect)

engine_lite = create_engine('sqlite:///database.db')
print(engine_lite.dialect)

