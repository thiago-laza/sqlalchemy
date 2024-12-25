from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    PrimaryKeyConstraint,
    String,
    Table,
)
from sqlalchemy.orm import registry

mapper_registry = registry()

t = Table(
    'comments',
    mapper_registry.metadata,
    Column('id', Integer(), nullable=False),
    Column('name', String(), nullable=False),
    Column('comment', String(), nullable=False),
    Column('live', String(), nullable=False),
    Column('created_at', DateTime(), nullable=True),
    PrimaryKeyConstraint('id'),
)


class Comment:
    pass


mapper_registry.map_imperatively(Comment, t)


'''
1. Importa os módulos necessários para criar a tabela e mapear
   a classe para o banco de dados:
   - 'Column', 'DateTime', 'Integer', 'PrimaryKeyConstraint', 'String' e 'Table'
     para definir a estrutura da tabela.
   - 'registry' para registrar o mapeamento da classe.

2. Cria um objeto de registro 'mapper_registry', que será usado
   para armazenar a metadata do banco de dados e o mapeamento da tabela.

3. Define a tabela 'comments' com as seguintes colunas:
   - 'id' (Integer), não pode ser nulo, com chave primária.
   - 'name' (String), não pode ser nulo.
   - 'comment' (String), não pode ser nulo.
   - 'live' (String), não pode ser nulo.
   - 'created_at' (DateTime), pode ser nulo (se não for fornecido).

4. Define a chave primária na coluna 'id' usando 'PrimaryKeyConstraint'.

5. Define a classe 'Comment', mas sem nenhum atributo ou comportamento
   definido (somente uma classe vazia no momento).

6. Usa 'mapper_registry.map_imperatively' para mapear a classe 'Comment'
   à tabela 'comments' criada acima. Isso permite que a classe 'Comment'
   seja usada como um modelo de objeto no código Python, com a tabela
   'comments' sendo mapeada no banco de dados.
'''
