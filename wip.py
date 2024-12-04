from sqlalchemy import create_engine

engine = create_engine(#factory: fabrica de motores p/ se conectar com sqlalchemy
    'sqlite://'
)

print(engine)
print(engine.dialect)