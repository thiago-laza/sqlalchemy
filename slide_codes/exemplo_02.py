from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')
print(engine.pool)

con_1 = engine.connect()

print(engine.pool.status())

con_2 = engine.connect()

print(engine.pool.status())

con_1.close()

print(engine.pool.status())

con_3 = engine.connect()

print(engine.pool.status())

'''
Este exemplo explora o uso de **pooling** no SQLAlchemy, 
que gerencia as conexões ao banco de dados para melhorar 
a eficiência e o desempenho.

Explicação:
1. **`engine.pool`**:
   - Exibe o tipo de pool configurado para o engine. Aqui, 
   é um `QueuePool`, o tipo de pool padrão no SQLAlchemy.
   - Um `QueuePool` mantém um número limitado de conexões 
   abertas, reutilizando-as conforme necessário.

2. **`engine.pool.status()`**:
   - Retorna o status atual do pool, incluindo:
     - **`Pool size`**: Número máximo de conexões permitidas no 
     pool.
     - **`Connections in pool`**: Conexões disponíveis no pool.
     - **`Current Overflow`**: Número de conexões extras 
     (além do tamanho do pool) atualmente abertas.
     - **`Checked out connections`**: Conexões ativamente em uso.

3. A sequência de operações:
   - **`con_1 = engine.connect()`**:
     - Abre a primeira conexão. O pool começa com 0 conexões 
     disponíveis, e 1 conexão é marcada como "em uso".
   - **`con_2 = engine.connect()`**:
     - Abre a segunda conexão. O pool ainda não contém conexões 
     disponíveis, e agora há 2 conexões "em uso".
   - **`con_1.close()`**:
     - Fecha a primeira conexão. Esta conexão volta ao pool, 
     tornando-se disponível para reutilização.
   - **`con_3 = engine.connect()`**:
     - Reutiliza a conexão disponível no pool, mantendo 2 
     conexões ativamente "em uso".

Saída explicada:
1. **`<sqlalchemy.pool.impl.QueuePool object at ...>`**:
   - Indica o uso de um `QueuePool` para gerenciar conexões.
2. **Status do pool ao longo das operações**:
   - Primeiro, 1 conexão em uso; nenhuma disponível no pool.
   - Depois, 2 conexões em uso; nenhuma disponível.
   - Após fechar `con_1`, uma conexão retorna ao pool.
   - Na última operação, o pool reutiliza a conexão disponível.

Contexto:
Pooling é útil para aplicações com alto tráfego, 
reduzindo a sobrecarga de abrir e fechar conexões 
repetidamente. O SQLAlchemy gerencia isso automaticamente, 
garantindo eficiência e controle.
'''