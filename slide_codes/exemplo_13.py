from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    ...


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    comment = Column(String, nullable=False)
    live = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self) -> str:
        return f'Comment({self.id=}, {self.name=}, {self.comment=}, {self.live=}, {self.created_at=})'


Comment(name='dunossauro', comment='LLL', live='youtube')

# from sqlalchemy import create_engine, select

# engine = create_engine(
#     'postgresql+psycopg://app_user:app_password@localhost:5432/app_db'
# )

# from sqlalchemy.orm import Session

# with Session(engine) as s:
#     result = s.scalars(select(Comment))
#     print(result.fetchmany(3))



'''
Este código define uma classe mapeada para a tabela 'comments'.

1. Importa os módulos necessários da SQLAlchemy.
2. Define a classe 'Base' que herda de 'DeclarativeBase',
   permitindo a definição de modelos mapeados para o banco de 
   dados.
   
3. A classe 'Comment' mapeia a tabela 'comments' no banco de dados.
   
4. Define as colunas da tabela:
   - 'id': chave primária e tipo Integer.
   - 'name': tipo String, não nula.
   - 'comment': tipo String, não nula.
   - 'live': tipo String, não nula.
   - 'created_at': tipo DateTime, valor padrão 'now'.

5. O método '__repr__' define a representação em string
   da instância da classe, exibindo os valores das colunas.

6. Criação de um objeto 'Comment' com valores
   atribuídos às colunas 'name', 'comment', e 'live'.

Comentários de código comentados indicam a criação
da engine de conexão e o uso da 'Session' para
interagir com o banco de dados, buscando resultados.
'''
