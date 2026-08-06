import asyncio
import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")
host = os.getenv("DB_HOST")

class TaskRepo:
    def __init__(self,conn):
        self.conn=conn
    async def create_task(self,title):
        return await self.conn.execute("""insert into tasks(title) values($1) returning *""",title)

    async def get_task(self,task_id):
        return await self.conn.fetchrow("""select * from tasks where id=$1""",task_id)

    async def list_tasks(self):
        return await self.conn.fetch("""select * from tasks""")

    async def count_tasks(self):
        return await self.conn.fetchval("""select count(*) from tasks""")


async def main():
    conn = await asyncpg.connect(user=user,password=password,database=database,host=host)

    repo = TaskRepo(conn)

    created_task=await repo.create_task('Learn RAG')
    print(created_task)

    task = await repo.get_task(2)
    print(task)

    tasks = await repo.list_tasks()
    print(tasks)

    count = await repo.count_tasks()
    print(count)


    await conn.close()

asyncio.run(main())