from sqlalchemy import create_engine, text

# Criação da engine
engine = create_engine('postgresql+psycopg2://postgres:lazevedo@localhost:5432/exemplo_sqlalchemy')

# Query base corrigida
query = 'SELECT id, name, comment FROM comments LIMIT 10 OFFSET {of}'

# Conexão com o banco de dados
with engine.connect() as connection:
    with connection.begin():
        # Executa a consulta para offset 0
        sql = text(query.format(of=0))
        result1 = connection.execute(sql)
        for row in result1:
            print(row)
    with connection.begin():
        # Executa a consulta para offset 10
        sql = text(query.format(of=1))
        result2 = connection.execute(sql)
        for row in result2:
            print(row)
    with connection.begin():
        # Executa a consulta para offset 20
        sql = text(query.format(of=2))
        result3 = connection.execute(sql)
        for row in result3:
            print(row)




'''
Este exemplo demonstra o uso de transações explícitas 
\com **`connection.begin()`** para manipular múltiplas 
consultas ao banco de dados, aplicando paginação com os 
parâmetros `LIMIT` e `OFFSET`.

---

### Explicação do código:

1. **Consulta SQL com `LIMIT` e `OFFSET`**:
   - O parâmetro `LIMIT` restringe o número de linhas retornadas.
   - O parâmetro `OFFSET` pula um número específico de 
   linhas antes de começar a retornar os resultados.
   - Aqui, `OFFSET` varia entre 0, 1 e 2 para alterar os 
   dados retornados.

2. **Transações explícitas**:
   - Cada bloco `with connection.begin()` inicia uma transação 
   explícita:
     - Garante que todas as operações dentro do bloco sejam 
     tratadas como uma unidade.
     - Ao final do bloco, um `COMMIT` é executado automaticamente.
   - Diferente de transações implícitas, que acontecem 
   automaticamente em consultas de leitura.

3. **Iteração sobre os resultados**:
   - Cada execução de consulta retorna um conjunto de 
   linhas que é iterado e exibido no console.

4. **Conexão gerenciada com `with`**:
   - O uso de `with engine.connect()` gerencia a conexão 
   e a encerra automaticamente ao final do bloco.

---

Saída:
O código imprime três conjuntos de resultados, cada um 
começando em posições diferentes devido ao uso do `OFFSET`:
- **Primeira consulta** (`OFFSET = 0`):
  ```
  (1, 'Exemplo 1', 'Comentário do exemplo 1')
  (2, 'Exemplo 2', 'Comentário do exemplo 2')
  (3, 'Exemplo 3', 'Comentário do exemplo 3')
  (4, 'Exemplo 4', 'Comentário do exemplo 4')
  (5, 'Exemplo 5', 'Comentário do exemplo 5')
  ```
- **Segunda consulta** (`OFFSET = 1`):
  ```
  (2, 'Exemplo 2', 'Comentário do exemplo 2')
  (3, 'Exemplo 3', 'Comentário do exemplo 3')
  (4, 'Exemplo 4', 'Comentário do exemplo 4')
  (5, 'Exemplo 5', 'Comentário do exemplo 5')
  ```
- **Terceira consulta** (`OFFSET = 2`):
  ```
  (3, 'Exemplo 3', 'Comentário do exemplo 3')
  (4, 'Exemplo 4', 'Comentário do exemplo 4')
  (5, 'Exemplo 5', 'Comentário do exemplo 5')
  ```

---

### Diferenças em relação aos exemplos anteriores:
1. **Transações explícitas**:
   - Este exemplo utiliza `connection.begin()` para gerenciar 
   transações de forma manual.
   - Nos exemplos anteriores, transações eram implícitas ou 
   gerenciadas pelo SQLAlchemy.

2. **Paginação**:
   - Aplica os conceitos de `LIMIT` e `OFFSET` para manipular 
   conjuntos de dados retornados.
   - Nos exemplos anteriores, nenhuma limitação ou offset foi 
   utilizado nas consultas.

3. **Execução múltipla de consultas**:
   - Três consultas diferentes são executadas no mesmo bloco 
   de conexão.
   - Nos exemplos anteriores, apenas uma consulta por conexão 
   era executada.

---

### Semelhanças:
1. Uso de `text` para criar as consultas SQL.
2. Logs detalhados com `echo=True`, mostrando operações de 
conexão, execução de consultas e commits.
3. Estrutura básica de conexão com o banco, utilizando 
`with engine.connect()`.

---

### Vantagens deste exemplo:
1. **Maior controle sobre transações**:
   - Permite agrupar operações em uma mesma transação, 
   garantindo consistência.

2. **Flexibilidade**:
   - Demonstra como realizar múltiplas consultas no mesmo 
   bloco de conexão.

3. **Eficiência**:
   - Utiliza a mesma conexão para executar várias consultas, 
   reduzindo o overhead de criar novas conexões.

---

### Considerações:
- Este exemplo é útil para cenários onde a manipulação 
explícita de transações é necessária ou quando é preciso 
executar múltiplas operações de forma eficiente na mesma conexão.
'''