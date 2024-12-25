from sqlalchemy import create_engine

engine_pg = create_engine('postgresql+psycopg2://lazah:lazevedo@localhost:5432/exemplo_sqlalchemy')
print(engine_pg.dialect)

engine_lite = create_engine('sqlite:///database.db')
print(engine_lite.dialect)

'''
Este exemplo demonstra como o SQLAlchemy gerencia diferentes 
dialetos de banco de dados ao criar engines. 

Explicação:
1. **`engine_pg`**:
   - Cria um engine para um banco de dados PostgreSQL usando 
   o driver `psycopg2`.
   - A URL de conexão segue o formato:  
     `postgresql+psycopg2://<usuario>:<senha>@<host>:<porta>/<banco>`
   - No exemplo:  
     - Usuário: `lazah`  
     - Senha: `lazevedo`  
     - Host: `localhost`  
     - Porta: `5432`  
     - Banco: `exemplo_sqlalchemy`
   - O método `engine_pg.dialect` retorna o dialeto associado 
   ao PostgreSQL (neste caso, o `PGDialect_psycopg2`).

2. **`engine_lite`**:
   - Cria um engine para um banco de dados SQLite com o arquivo 
   `database.db`.
   - O método `engine_lite.dialect` retorna o dialeto associado 
   ao SQLite (`SQLiteDialect_pysqlite`).

Saída:
- **`PGDialect_psycopg2`**: 
Representa o dialeto PostgreSQL, responsável por traduzir 
comandos SQL do SQLAlchemy para a sintaxe específica do 
PostgreSQL.
- **`SQLiteDialect_pysqlite`**: 
Representa o dialeto SQLite, adaptado para o driver `pysqlite`.
- Cada objeto `dialect` reflete como o SQLAlchemy interage com 
o respectivo banco de dados.

Esse exemplo destaca a portabilidade do SQLAlchemy, 
permitindo trabalhar com diferentes sistemas de banco de 
dados através de dialetos apropriados.
'''

