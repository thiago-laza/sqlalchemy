import sqlalchemy as sa

metadata = sa.MetaData()

t = sa.Table(
    'comments',
    metadata,
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('comment', sa.String(), nullable=False),
    sa.Column('live', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
)

engine = sa.create_engine('sqlite://')

metadata.create_all(engine)

with engine.connect() as con:
    with con.begin():
        con.execute(
            sa.text(
                f"""
                insert into comments (name, comment, live, created_at)
                values ('dunossauro', 'alow', 'youtube', '2024-01-10 12:50:47.35297');
                """
            )
        )

    with con.begin():
        result = con.execute(sa.text('select * from comments'))
        print(result.fetchall())


'''
Este exemplo demonstra como criar uma tabela usando SQLAlchemy, 
inserindo dados nela e consultando a tabela para verificar 
os dados inseridos. Aqui, usamos a API de SQLAlchemy para 
definir o esquema da tabela de maneira programática e 
executar operações SQL diretamente.

Explicação do código:

1. **Definição do Esquema da Tabela**:
   - `sa.MetaData()` é usado para armazenar o esquema de tabelas.
   - A tabela `comments` é definida com as colunas `id`, `name`, 
   `comment`, `live`, e `created_at`. O `id` é a chave primária.
   - Cada coluna é definida com um tipo de dados 
   apropriado (e.g., `Integer`, `String`, `DateTime`).
   
2. **Criação do Banco de Dados**:
   - O comando `sa.create_engine('sqlite://')` cria um banco 
   de dados SQLite em memória, sem a necessidade de um arquivo 
   físico. O banco de dados será volátil e desaparecerá após a 
   execução.
   - `metadata.create_all(engine)` cria a tabela no banco de 
   dados, usando a definição fornecida.

3. **Inserção de Dados**:
   - Dentro de uma transação (usando `with con.begin()`), um 
   comando SQL de inserção é executado para adicionar um 
   registro à tabela `comments`.

4. **Consulta e Exibição de Dados**:
   - Após inserir os dados, uma consulta SQL `select * from 
   comments` é executada para recuperar todos os registros da 
   tabela.
   - O método `fetchall()` retorna todas as linhas, que são 
   impressas na tela.


Saída:
A saída mostrará os dados inseridos na tabela `comments`, como 
no exemplo abaixo:
```
[(1, 'dunossauro', 'alow', 'youtube', datetime.datetime(2024, 1, 10, 12, 50, 47, 352970))]
```

Observações:
- **Uso de `sa.Table` e `sa.MetaData`**: Essa abordagem oferece 
maior flexibilidade em relação à definição de tabelas e 
manipulação de dados diretamente no código, sem necessidade 
de definir modelos ORM, como em outros exemplos.
- **`sa.text` para SQL Dinâmico**: O uso de `sa.text()` 
permite escrever SQL diretamente no código, o que é útil 
para consultas e operações que não requerem a abstração do ORM.

### Diferenças em relação aos exemplos anteriores:
1. **Definição de Tabelas**: Ao invés de trabalhar com comandos 
SQL diretamente ou com objetos ORM, aqui criamos a tabela 
explicitamente usando `sa.Table` e definindo cada coluna.
2. **Criação e Manipulação de Esquema**: O exemplo 08 inclui 
a criação de tabelas no banco de dados, algo que não foi 
feito nos exemplos anteriores.
3. **Execução de SQL Direto**: A consulta e a inserção de 
dados são feitas diretamente com SQL, sem usar a API ORM, 
diferentemente dos exemplos anteriores, que usavam objetos 
Python para interagir com o banco de dados.

### Semelhanças:
1. **Uso do SQLAlchemy para Conectar e Executar Comandos**: 
Todos os exemplos utilizam `create_engine()` para estabelecer 
a conexão e realizar operações no banco de dados.
2. **Transações**: Como nos exemplos anteriores, operações 
de banco de dados são feitas dentro de transações  
(`with con.begin()`), o que garante que as operações 
sejam atômicas e sejam revertidas automaticamente em caso 
de falha.

### Vantagens:
- **Flexibilidade**: Definir a tabela diretamente no código 
oferece mais controle sobre a estrutura do banco de dados.
- **Execução de SQL Puro**: A execução de SQL direto com `
sa.text()` é útil quando precisamos de comandos SQL 
personalizados que não podem ser facilmente representados 
com ORM.
  
### Considerações:
- **Banco de Dados em Memória**: O uso de `sqlite://` 
cria um banco de dados em memória, o que significa que 
os dados serão perdidos após a execução do script. Isso 
é ideal para testes e demonstrações rápidas, mas para 
persistência, seria necessário especificar um caminho 
de arquivo SQLite ou outro banco de dados persistente.
'''