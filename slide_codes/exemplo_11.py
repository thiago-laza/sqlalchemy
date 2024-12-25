from sqlalchemy import MetaData, Table, create_engine, select

engine = create_engine('postgresql+psycopg2://postgres:lazevedo@localhost:5432/exemplo_sqlalchemy')

metadata = MetaData()

comments = Table('comments', metadata, autoload_with=engine)

with engine.connect() as con:
    stmt = (
        select(comments)
        .where(
            (
                (comments.c.name == 'Eduardo Mendes')
                | (comments.c.name == 'dunossauro')
            )
            & ((comments.c.live == 'youtube') | (comments.c.live == 'twitch'))
        )
        .limit(3)
        .offset(0)
        .order_by(comments.c.id)
    )
    print(stmt)

    result = con.execute(stmt)
    print(result.all())

 
'''
Este código cria uma conexão com um banco de dados PostgreSQL 
usando a SQLAlchemy. 
Primeiro, é criada uma engine para se conectar ao banco 
de dados especificado pela URL, que inclui as credenciais de acesso.

Em seguida, um objeto 'MetaData' é instanciado para gerenciar 
informações sobre o esquema do banco de dados. A tabela 
'comments' é carregada automaticamente a partir do banco 
de dados usando 'autoload_with=engine', que permite que a 
SQLAlchemy busque a definição da tabela diretamente no banco 
de dados.

Na sequência, uma consulta SQL é construída utilizando o 
método 'select()' da SQLAlchemy. A consulta seleciona os 
registros da tabela 'comments' com algumas condições específicas:

- Filtra os registros onde o nome seja 'Eduardo Mendes' 
ou 'dunossauro' e, ao mesmo tempo, a coluna 'live' tenha 
valor 'youtube' ou 'twitch'.

- Limita os resultados a 3 registros com a cláusula '.limit(3)'.
- Usa '.offset(0)' para começar do primeiro registro.
- Ordena os resultados pela coluna 'id' da tabela 'comments'.

A consulta gerada é então executada e os resultados são impressos.

O uso de 'select(comments)' e a sintaxe para condições de filtro, ordenação e limitação fazem com que a consulta seja executada de forma eficiente com base nas condições fornecidas.
'''

