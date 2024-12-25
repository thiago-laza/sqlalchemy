from datetime import datetime
from select import select
from sqlalchemy import create_engine, func, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

class Base(DeclarativeBase):
    pass

class Comment(Base):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    comment: Mapped[str] = mapped_column(Text, nullable=False)
    live: Mapped[str] = mapped_column(String(50), nullable=True)  # Limite de 50 caracteres
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)

    def __repr__(self) -> str:
        return f'Comment({self.id=}, {self.name=}, {self.comment=}, {self.live=}, {self.created_at=})'

# Criar uma instância de Comment e adicioná-la ao banco de dados
new_comment = Comment(name='User 1', comment='Comment 1', live='youtube')

# Configuração da engine com a URL correta do banco
engine = create_engine('postgresql+psycopg2://postgres:your_password@localhost:5432/exemplo_sqlalchemy')

# Inserir o novo comentário na tabela
with Session(engine) as s:
    s.add(new_comment)  # Adiciona o novo comentário
    s.commit()  # Comita a transação para persistir os dados

# Recuperando dados do banco de dados
with Session(engine) as s:
    result = s.scalars(select(Comment))
    print(result.fetchmany(3))


#ERRO DE AUTENTICACO COM O BANCO

'''
1. Importa a classe 'datetime' para manipulação de datas e horas.
   
2. Importa 'func' para usar funções do banco de dados (como 'now').
   
3. Importa 'DeclarativeBase', 'Mapped' e 'mapped_column' para definir
   classes mapeadas e colunas no SQLAlchemy com tipo forte.
   
4. A classe 'Base' herda de 'DeclarativeBase', permitindo que as classes
   definam modelos mapeados diretamente para o banco de dados.

5. A classe 'Comment' é mapeada para a tabela 'comments' no banco de dados.
   
6. As colunas da tabela são definidas com tipos mapeados:
   - 'id' como chave primária (Integer).
   - 'name' (String), 'comment' (String), 'live' (String).
   - 'created_at' (DateTime) com valor padrão 'now' (func.now()).
   
7. O método '__repr__' define a representação de string da instância.
   Exibe os valores das colunas como uma string legível.
   
8. Cria uma instância da classe 'Comment' com valores para as colunas
   'name', 'comment' e 'live'. Porém, essa instância não é inserida
   no banco de dados diretamente.

9. Cria uma conexão com o banco de dados PostgreSQL através da engine
   configurada, usando a URL de conexão do banco.

10. Cria uma 'Session' para interagir com o banco de dados.
   
11. Usa 'Session' para executar uma consulta (select) na tabela 'comments'.
    O método 'scalars' retorna os resultados de forma otimizada.
    
12. Exibe os três primeiros resultados da consulta com 'fetchmany(3)'.
    O resultado é impresso na tela.
'''
