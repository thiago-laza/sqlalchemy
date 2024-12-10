from asyncio import run

from sqlalchemy import create_engine, text

from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine('postgresql+asyncpg://lazah:lazevedo@localhost:5432/exemplo_sqlalchemy', echo=True)


async def main():
    async with engine.connect() as connection:
        sql = text('SELECT id, name, comments FROM my_table')
        result = await connection.execute(sql)
        for row in result:
            print(row)

run(main())