import asyncpg

from core.config import PG_USER, PG_PASSWORD, PG_DATABASE, PG_HOST, PG_PORT, PG_COMMAND_TIMEOUT


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_data(self, user_id: int, user_name: str):
        query = f"""
        insert into users_data (id, username) 
        values ({user_id}, '{user_name}') on conflict (id) do update set username='{user_name}'
        """
        await self.connector.execute(query)


async def create_pool():
    return await asyncpg.create_pool(user=PG_USER, password=PG_PASSWORD,
                                     database=PG_DATABASE, host=PG_HOST,
                                     port=PG_PORT, command_timeout=PG_COMMAND_TIMEOUT)
