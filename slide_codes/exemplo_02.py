from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')
print(engine.pool)

con_1 = engine.connect()

print(engine.pool.status())

con_2 = engine.connect()

print(engine.pool.status())

con_1.close()

print(engine.pool.status())

con_3 = engine.connect()

print(engine.pool.status())