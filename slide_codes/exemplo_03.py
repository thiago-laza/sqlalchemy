from sqlalchemy import create_engine, text


engine = create_engine('postgresql+psycopg2://postgres:lazevedo@localhost:5432/exemplo_sqlalchemy',echo=True)

connection = engine.connect()

sql = text('SELECT id, name, comment, live, created_at FROM comments')

result = connection.execute(sql)

for row in result:
    print(row)

connection.close()

'''
Este exemplo executa uma consulta SQL simples em um banco 
de dados PostgreSQL usando SQLAlchemy. Ele demonstra como 
criar e usar conexões, executar consultas, e processar os 
resultados.

Explicação:
1. **`create_engine`**:
   - Cria um engine para o banco de dados PostgreSQL com o 
   driver `psycopg2`.
   - O parâmetro `echo=True` habilita o log detalhado, exibindo 
   todas as operações SQL geradas.

2. **`engine.connect()`**:
   - Estabelece uma conexão com o banco de dados usando o engine.

3. **`text('SELECT id, name, comments FROM my_table')`**:
   - Prepara uma consulta SQL para selecionar as colunas `id`,
    `name` e `comments` da tabela `my_table`.
   - A função `text` é usada para criar objetos SQL de maneira 
   segura e compatível com o SQLAlchemy.

4. **`connection.execute(sql)`**:
   - Executa a consulta no banco de dados.
   - Retorna um objeto `Result` contendo os dados da consulta.

5. **Iteração sobre os resultados**:
   - Cada linha do resultado é uma tupla com os valores 
   das colunas selecionadas.  
   - O loop imprime cada linha da consulta.

6. **`connection.close()`**:
   - Fecha a conexão com o banco de dados.

7. **Log detalhado (saída)**:
   - Mostra as etapas internas executadas pelo SQLAlchemy:
     - Checagem do esquema (`current_schema()`).
     - Configurações específicas do PostgreSQL.
     - Execução da consulta SQL.
     - Operações de controle de transação (`BEGIN` e `ROLLBACK`).

### Saída do código:
- Os registros de `my_table` são exibidos como tuplas:
  ```
  (1, 'Exemplo 1', 'Comentário do exemplo 1')
  (2, 'Exemplo 2', 'Comentário do exemplo 2')
  (3, 'Exemplo 3', 'Comentário do exemplo 3')
  (4, 'Exemplo 4', 'Comentário do exemplo 4')
  (5, 'Exemplo 5', 'Comentário do exemplo 5')
  ```
  
- **Por que um `ROLLBACK`?**  
   - O SQLAlchemy inicia uma transação automaticamente ao 
   executar consultas. Como nenhuma alteração no banco foi 
   feita (somente leitura), a transação é revertida (rollback) 
   no final.

### Contexto:
Este exemplo mostra como realizar consultas de leitura no 
banco de dados e processar os resultados. O log detalhado é 
útil para depuração, permitindo entender todas as operações 
executadas pelo SQLAlchemy.
'''