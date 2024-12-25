from sqlalchemy import create_engine, text

# Configuração da engine para conectar ao banco de dados
engine = create_engine('postgresql+psycopg2://postgres:lazevedo@localhost:5432/exemplo_sqlalchemy')

# Conexão com o banco de dados
with engine.connect() as con:
    
    # Consulta corrigida para a tabela 'comments'
    sql = text('SELECT comment FROM comments')
    
    # Executa a consulta e obtém o primeiro valor
    result = con.execute(sql)
    primeiro_valor = result.fetchone()
    if primeiro_valor:
        print("Primeiro valor referente à coluna 'comment':", primeiro_valor.comment)
    else:
        print("Nenhum valor encontrado na tabela.")

    # Executa novamente a consulta para obter todos os valores
    result = con.execute(sql)  
    todos_os_valores = result.fetchall()
    print("\nTodos os valores da coluna 'comment':")
    for row in todos_os_valores:
        print(row.comment)


'''
Este exemplo explora o uso de métodos para acessar os 
resultados de consultas no SQLAlchemy, utilizando `fetchone` 
para obter uma única linha e `fetchall` para recuperar todas 
as linhas. Ele também destaca a capacidade de reutilizar 
consultas com `text` no mesmo contexto de conexão.

---

Explicação do código:

1. **Consulta SQL**:
   - Seleciona apenas a coluna `comments` da tabela `my_table`.

2. **`fetchone`**:
   - Obtém apenas a primeira linha do conjunto de resultados.
   - Retorna um objeto semelhante a uma tupla, acessível tanto 
   por índices como por nomes das colunas 
   (ex.: `primeiro_valor.comments`).

3. **Reexecução da consulta**:
   - A consulta é reexecutada para obter todos os valores 
   com `fetchall`.
   - Isso é necessário porque, após chamar `fetchone`, o 
   cursor está posicionado na próxima linha do conjunto 
   de resultados, e os dados anteriores não podem ser 
   recuperados sem reexecutar a consulta.

4. **`fetchall`**:
   - Retorna todas as linhas restantes como uma lista de objetos.
   - Iteramos sobre as linhas para exibir os valores da 
   coluna `comments`.

5. **Gerenciamento de conexão com `with`**:
   - A conexão é gerenciada automaticamente e fechada ao sair 
   do bloco.

6. **Log detalhado**:
   - Com `echo=True`, o SQLAlchemy exibe os logs das operações, 
   incluindo o tempo de cache entre reexecuções da mesma consulta.

---

### Saída:
1. Exibição do primeiro valor:
   ```
   Primeiro valor referente à coluna 'comments': Comentário do 
   exemplo 1
   ```

2. Exibição de todos os valores:
   ```
   Todos os valores da coluna 'comments':
   Comentário do exemplo 1
   Comentário do exemplo 2
   Comentário do exemplo 3
   Comentário do exemplo 4
   Comentário do exemplo 5
   ```

---

### Diferenças em relação aos exemplos anteriores:
1. **Uso de `fetchone` e `fetchall`**:
   - Este exemplo demonstra métodos específicos para acessar os 
   resultados de consultas.
   - Nos exemplos anteriores, as linhas eram iteradas 
   diretamente no resultado da consulta.

2. **Reexecução da consulta**:
   - O mesmo SQL é executado duas vezes para demonstrar 
   diferentes formas de acessar os dados.
   - Isso não ocorreu nos exemplos anteriores, que executavam 
   cada consulta apenas uma vez.

---

### Semelhanças:
1. Uso de `text` para criar a consulta SQL.
2. Gerenciamento automático de conexões com o bloco `with`.
3. Logs detalhados mostrando a execução de SQL e transações.

---

### Vantagens deste exemplo:
1. **Controle sobre os dados retornados**:
   - Permite obter apenas uma linha (com `fetchone`) ou todas 
   as linhas (com `fetchall`), dependendo da necessidade.
   - Evita carregar todos os resultados na memória quando não 
   necessário.

2. **Demonstrativo de reuso de consultas**:
   - Ilustra como reexecutar a mesma consulta no mesmo contexto 
   de conexão.

3. **Leitura semântica dos dados**:
   - As colunas podem ser acessadas diretamente pelos seus 
   nomes no objeto retornado, o que melhora a clareza do código.

---

### Considerações:
- Este exemplo é útil para cenários onde o controle granular 
sobre os dados retornados é necessário, como quando queremos 
processar apenas uma parte dos resultados antes de carregar 
todos os dados.
'''




