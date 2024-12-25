from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db', echo=True)

connection = engine.connect()
print(connection.connection.dbapi_connection)
connection.close()



'''
Este exemplo mostra como abrir e fechar uma conexão com o 
banco de dados usando o SQLAlchemy e inclui uma 
configuração para exibir logs das operações executadas.

Explicação:

1. **`create_engine('sqlite:///database.db', echo=True)`**:
Cria o engine para o banco de dados SQLite, mas agora com o 
parâmetro `echo=True`. Isso habilita logs detalhados das 
instruções SQL geradas pelo SQLAlchemy, úteis para depuração.

2. **`engine.connect()`**: 
Abre uma conexão com o banco de dados através do engine.

3. **`connection.connection.dbapi_connection`**: 
Acessa a conexão do nível mais baixo (do driver DBAPI) 
usada pelo SQLAlchemy. Neste caso, o driver do SQLite 
é o `sqlite3`, e o objeto exibido é a instância da 
conexão do SQLite.

4. **`connection.close()`**: 
Fecha a conexão explicitamente. É uma boa prática 
garantir que conexões sejam encerradas quando não forem 
mais necessárias.

Saída:
- **`<sqlite3.Connection object at 0x...>`**: 
Representa o objeto da conexão SQLite. O endereço de 
memória (`0x740533687100`) varia em cada execução.


- Este código demonstra como trabalhar diretamente com 
conexões no SQLAlchemy, enquanto mantém o controle sobre 
sua abertura e fechamento.
'''