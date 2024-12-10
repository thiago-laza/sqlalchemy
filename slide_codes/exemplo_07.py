from sqlalchemy import create_engine, text

engine = create_engine('postgresql+psycopg2://lazah:lazevedo@localhost:5432/exemplo_sqlalchemy', echo=True)

with engine.connect() as con:
    # Consulta para selecionar apenas a coluna 'comments'
    sql = text('SELECT comments FROM my_table')
    result = con.execute(sql)

    # Recupera o primeiro valor da coluna 'comments'
    primeiro_valor = result.fetchone()
    if primeiro_valor:
        print("Primeiro valor referente à coluna 'comments':", primeiro_valor.comments)
    else:
        print("Nenhum valor encontrado na tabela.")

    # Recupera todos os valores restantes da coluna 'comments'
    result = con.execute(sql)  # Executa novamente a consulta para obter todos os valores
    todos_os_valores = result.fetchall()
    print("\nTodos os valores da coluna 'comments':")
    for row in todos_os_valores:
        print(row.comments)





