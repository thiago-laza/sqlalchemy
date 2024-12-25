from sqlalchemy import create_engine, text

engine = create_engine('postgresql+psycopg2://postgres:lazevedo@localhost:5432/exemplo_sqlalchemy')

with engine.connect() as connection:
    sql = text('SELECT id, name, comment, live, created_at FROM comments')
    result = connection.execute(sql)
    for row in result:
        print(row)



'''
Este exemplo utiliza um **context manager (`with`)** para 
gerenciar automaticamente a conexão com o banco de dados, 
tornando o código mais limpo e menos propenso a erros.

Explicação:
1. **`with engine.connect() as connection`**:
   - O **context manager** abre a conexão com o banco de dados 
   e garante que ela será fechada automaticamente no final do 
   bloco, mesmo que ocorra uma exceção.
   - Elimina a necessidade de chamar `connection.close()` 
   manualmente.

2. **Restante do código**:
   - É idêntico ao exemplo 03:
     - A consulta SQL é preparada com `text`.
     - A consulta é executada com `connection.execute(sql)`.
     - O resultado é iterado, imprimindo as linhas da tabela.

3. **Logs (`echo=True`)**:
   - Detalham as operações realizadas pelo SQLAlchemy, como 
   em **exemplo 03**:
     - Verificação do esquema.
     - Configurações de conexão.
     - Execução da consulta SQL.
     - Início e encerramento de uma transação.

---

Saída:
- A saída é idêntica ao exemplo 03, exibindo os registros 
de `my_table`:
  ```
  (1, 'Exemplo 1', 'Comentário do exemplo 1')
  (2, 'Exemplo 2', 'Comentário do exemplo 2')
  (3, 'Exemplo 3', 'Comentário do exemplo 3')
  (4, 'Exemplo 4', 'Comentário do exemplo 4')
  (5, 'Exemplo 5', 'Comentário do exemplo 5')
  ```

---

Diferenças em relação ao exemplo 03:
1. **Uso de `with`**:
   - O exemplo 04 utiliza um **context manager** para gerenciar 
   a conexão, garantindo o fechamento automático.
   - O exemplo 03 requer o fechamento manual da conexão com 
   `connection.close()`.

2. **Segurança**:
   - O exemplo 04 reduz o risco de conexões não serem fechadas 
   caso ocorra um erro durante a execução.

3. **Legibilidade**:
   - O exemplo 04 é mais conciso e segue melhores práticas de 
   programação.

---

Semelhanças:
1. Ambos executam a mesma consulta SQL e exibem os mesmos 
resultados.
2. Ambos utilizam `create_engine` com `echo=True` para 
habilitar logs detalhados.
3. Ambos realizam uma transação de leitura (`SELECT`) e 
fazem `ROLLBACK` automaticamente após a execução.

### Conclusão:
O exemplo 04 é preferível para cenários práticos, pois 
facilita o gerenciamento de conexões e melhora a segurança 
do código.
'''