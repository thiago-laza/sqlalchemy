from asyncio import run
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine


engine = create_async_engine('postgresql+asyncpg://postgres:lazevedo@localhost:5432/exemplo_sqlalchemy')

async def main():
    async with engine.connect() as connection:
        
        sql = text('SELECT id, name, comment, live, created_at FROM comments')
        result = await connection.execute(sql)
        
        
        for row in result:
            print(row)


run(main())


'''
Este exemplo utiliza o SQLAlchemy AsyncIO para executar 
consultas de forma assíncrona, uma abordagem mais moderna 
e eficiente para aplicações que requerem alta simultaneidade. 
Ele apresenta diferenças significativas em relação aos 
exemplos 03 e 04, que utilizam conexões síncronas.

---

Diferenças em relação aos exemplos 03 e 04:

1. **Conexão Assíncrona**:
   - Aqui é usado o `create_async_engine` para criar um engine 
   assíncrono com o driver `asyncpg`.
   - Nos exemplos anteriores, `create_engine` cria engines 
   síncronos.

2. **Execução de código**:
   - Este exemplo utiliza a palavra-chave `async` e o método 
   `await` para manipular a execução de consultas.
   - Nos exemplos 03 e 04, as operações são síncronas e 
   bloqueiam a execução até serem concluídas.

3. **Loop de eventos**:
   - O código utiliza `asyncio.run()` para executar a função 
   assíncrona `main`.
   - Nos exemplos anteriores, o Python tradicional executa o 
   código linearmente.

4. **Context Manager Assíncrono**:
   - O bloco `async with` gerencia a conexão de maneira 
   assíncrona.
   - Nos exemplos 03 e 04, o contexto `with` ou o fechamento 
   manual da conexão é suficiente.

5. **Dependência de Driver**:
   - Requer o driver `asyncpg`, compatível com PostgreSQL.
   - Nos exemplos anteriores, o driver `psycopg2` é utilizado.

---

### Semelhanças:

1. **SQLAlchemy Core**:
   - A consulta SQL ainda é construída com `text`, sem 
   alterações significativas.
   
2. **Estrutura da execução**:
   - Consulta SQL `SELECT id, name, comments FROM my_table`.
   - Iteração sobre os resultados, imprimindo as linhas.

3. **Logs (`echo=True`)**:
   - Assim como nos exemplos anteriores, o log detalha as 
   operações executadas.

4. **Transações Automáticas**:
   - Uma transação é iniciada implicitamente (`BEGIN`) e 
   encerrada com um `ROLLBACK`, como nos exemplos anteriores.

---

### Vantagens do exemplo 05:

1. **Alta Concurrência**:
   - O modelo assíncrono permite que o programa manipule 
   múltiplas conexões ou tarefas simultaneamente, sem bloquear 
   o restante do código.
   - Ideal para aplicações web ou sistemas com grande número 
   de usuários simultâneos.

2. **Melhor Desempenho**:
   - Em cenários com operações de I/O intensivas 
   (como acesso a bancos de dados), a abordagem assíncrona 
   pode reduzir o tempo de resposta total.

3. **Escalabilidade**:
   - Permite o processamento eficiente de várias tarefas, 
   tornando-se mais adequado para sistemas distribuídos ou 
   microsserviços.

---

### Considerações:
- **Quando usar o exemplo 05?**
  - Em aplicações modernas com alto volume de acessos, 
  como APIs ou servidores web, onde o modelo assíncrono 
  melhora a eficiência.
- **Quando usar os exemplos 03 e 04?**
  - Em aplicações simples ou scripts pontuais onde a 
  sincronização não é um gargalo significativo. 

O exemplo 05 representa uma evolução natural para 
cenários onde o desempenho e a simultaneidade são críticos.
'''