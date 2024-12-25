from datetime import datetime

from sqlalchemy import (
    MetaData,
    Table,
    create_engine,
    delete,
    insert,
    select,
    update,
)


engine = create_engine('postgresql+psycopg2://postgres:lazevedo@localhost:5432/exemplo_sqlalchemy')
metadata = MetaData()

comments = Table('comments', metadata, autoload_with=engine)

with engine.connect() as con:
    with con.begin():
        stmt = insert(comments).values(
            name='dunossauro',
            comment='LLL',
            live='youtube',
            created_at=datetime.now(),
        )
        con.execute(stmt)

    with con.begin():
        stmt = (
            update(comments)
            .where(
                comments.c.name == 'dunossauro',
                comments.c.comment == 'LLL',
                comments.c.live == 'youtube',
            )
            .values(comment='Pei')
        )

        con.execute(stmt)

    with con.begin():
        stmt = select(comments).where(
            comments.c.name == 'dunossauro',
            comments.c.live == 'youtube',
            comments.c.comment == 'Pei',
        )
        results = con.execute(stmt)
        print(results.all())

    with con.begin():
        stmt = delete(comments).where(
            comments.c.name == 'dunossauro',
            comments.c.live == 'youtube',
            comments.c.comment == 'Pei',
        )
        con.execute(stmt)

    with con.begin():
        stmt = select(comments).where(
            comments.c.name == 'dunossauro',
            comments.c.live == 'youtube',
            comments.c.comment == 'Pei',
        )
        results = con.execute(stmt)
        print(results.all())



'''
Este código utiliza a SQLAlchemy para interagir com um banco 
de dados PostgreSQL, realizando várias operações 
CRUD (Create, Read, Update, Delete) em uma tabela 
chamada 'comments'. 

1. A biblioteca 'datetime' é importada para manipulação 
de datas e horas.
2. A SQLAlchemy é configurada para se conectar ao banco de 
dados usando a URL especificada. 
3. Um objeto 'MetaData' é criado e a tabela 'comments' 
é carregada automaticamente do banco de dados usando 
'autoload_with=engine', o que permite que a SQLAlchemy 
descubra a definição da tabela diretamente do banco de dados.

A seguir, são realizadas várias operações:

- **Insert (Criação):**
  - Um registro é inserido na tabela 'comments' com valores 
  para as colunas 'name', 'comment', 'live', e 'created_at' 
  (data e hora atual).
  
- **Update (Atualização):**
  - O registro inserido anteriormente é atualizado. A condição 
  de filtro utiliza os valores inseridos no 'name', 'comment', 
  e 'live'. O valor da coluna 'comment' é alterado para 'Pei'.
  
- **Select (Leitura):**
  - Após a atualização, é realizada uma consulta (select) 
  para verificar se o registro foi atualizado corretamente. 
  O filtro é aplicado para encontrar o registro com 'name' 
  igual a 'dunossauro', 'live' igual a 'youtube' e 'comment' 
  igual a 'Pei'. Os resultados são impressos.

- **Delete (Exclusão):**
  - O registro é então excluído da tabela 'comments' 
  utilizando as mesmas condições de filtro aplicadas na 
  consulta anterior.
  
- **Select (Leitura Final):**
  - Após a exclusão, uma nova consulta (select) é realizada 
  para verificar se o registro foi realmente removido da tabela. 
  A consulta não deve retornar nenhum resultado, já que o 
  registro foi excluído anteriormente.

Cada operação é realizada dentro de um bloco de transação 
com 'con.begin()', garantindo que todas as mudanças feitas 
sejam tratadas como transações, e as alterações no banco de 
dados sejam comitadas ou revertidas com base no sucesso ou 
falha da operação.
'''
