from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

reg = registry()


@reg.mapped_as_dataclass
class Comment:
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    comment: Mapped[str]
    live: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )


Comment(name='dunossauro', comment='LLL', live='youtube')

from sqlalchemy import create_engine, select

engine = create_engine('postgresql+psycopg2://postgres:lazevedo@localhost:5432/exemplo_sqlalchemy')

from sqlalchemy.orm import Session

with Session(engine) as s:
    result = s.scalar(select(Comment).where(Comment.id == 3))
    s.delete(result)
    s.commit()


'''
1. Importa a classe 'datetime' para manipulação de datas e horas.
   
2. Importa 'func' para utilizar funções do banco de dados, como 'now'.

3. Importa 'Mapped', 'mapped_column' e 'registry' para trabalhar com
   tipos fortemente mapeados e registrar o mapeamento de classes.
   
4. Cria um objeto de registro 'reg', que será usado para registrar
   as classes mapeadas para o banco de dados.

5. A classe 'Comment' é mapeada para a tabela 'comments' no banco de dados
   usando o decorador '@reg.mapped_as_dataclass'. Isso permite que a
   classe use as funcionalidades de uma dataclass e também seja mapeada para
   o banco de dados.
   
6. As colunas são definidas com tipos mapeados:
   - 'id' como chave primária (Integer), não inicializável.
   - 'name' (String), 'comment' (String), 'live' (String).
   - 'created_at' (DateTime), com valor padrão 'now' (func.now()), não inicializável.

7. Criação de uma instância da classe 'Comment', mas não salva no banco
   diretamente. Apenas cria uma instância de 'Comment' com dados.

8. Cria a engine de conexão para o banco de dados PostgreSQL com a URL
   fornecida, usando a biblioteca 'psycopg2' para a comunicação com o banco.

9. Usa 'Session' para interagir com o banco de dados, executando
   uma consulta 'select' para buscar o comentário com 'id' igual a 1.

10. Exclui o comentário encontrado com a consulta, usando 's.delete(result)'.

11. Comita a transação com 's.commit()', salvando a alteração no banco.
'''
