from sqlalchemy import create_engine

engine = create_engine(#factory: fabrica de motores p/ se conectar com sqlalchemy
    'sqlite://'
)

con =engine.connect()

con.close()
