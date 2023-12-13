import asyncio
from urllib.parse import urlparse, unquote

import asyncpg
import pytz


# execute: 이 메서드는 주로 INSERT, UPDATE, DELETE 등의 SQL 명령을 실행할 때 사용
# 이는 쿼리의 결과를 반환하지 않고, 대신 영향 받은 행의 수를 반환
# fetch: SELECT 쿼리를 실행하고 그 결과를 반환할 때 사용


class Repository:
    def __init__(self, db_url: str) -> None:
        self.tz = pytz.timezone("Asia/Seoul")
        self.conn = None
        self.db_url = db_url

    async def initialize(self):
        parsed_url = urlparse(self.db_url)
        db_name = parsed_url.path[1:]
        user = parsed_url.username
        password = unquote(parsed_url.password)
        host = parsed_url.hostname
        port = parsed_url.port
        self.conn = await asyncpg.connect(
            database=db_name, user=user, password=password, host=host, port=port
        )

    async def test_connection(self) -> bool:
        try:
            await self.conn.fetch("SELECT 1")
            return True
        except Exception:
            return False

    async def get_all_scraping_urls_by_group(self, group_id) -> list[dict]:
        try:
            sql = f"""
                select *
                from scraping_scrapingurl ss 
                where ss.scraping_group_id = {group_id}
            """
            result = await self.conn.fetch(sql)
            return [dict(record) for record in result]
        except Exception as e:
            print(e)

    async def get_all_scraping_groups(self) -> list[dict]:
        try:
            sql = """
                select *
                from scraping_scrapinggroup;
            """
            result = await self.conn.fetch(sql)
            return [dict(record) for record in result]
        except Exception as e:
            print(e)

    async def create_scraping_log_and_update_scraping_url(
        self, scraping_url_id: int, response: str, is_error: bool
    ) -> None:
        try:
            insert_scraping_log_sql = f"""
                INSERT INTO scraping_scrapinglog (result, is_error, created_at, updated_at) 
                VALUES ('{response}', {is_error}, NOW(), NOW())
                RETURNING id;
            """
            new_scraping_log_pk: int = await self.conn.fetchval(
                insert_scraping_log_sql
            )  # ID값을 반환받음

            update_scraping_url_sql = f"""
                UPDATE scraping_scrapingurl
                SET last_scraping_log = {new_scraping_log_pk}
                WHERE id = {scraping_url_id};
            """
            await self.conn.execute(update_scraping_url_sql)
        except Exception as e:
            print(e)
            return None

    async def update_scrapingurl_with_log_id(self, scraping_url_id: int, log_id: int):
        try:
            sql = f"""
                UPDATE scrapingurl
                SET log_id = {log_id}
                WHERE id = {scraping_url_id};
            """
            await self.conn.execute(sql)
        except Exception as e:
            print(e)

    async def diff_check_two_scraping_log(self):
        ...

    async def close(self):
        if self.conn:
            await self.conn.close()


async def main():
    db_url = "db_url"
    rep = Repository(db_url)
    await rep.initialize()
    connection_successful = await rep.test_connection()
    print("Connection Successful:", connection_successful)
    scraping_urls: list[dict] = await rep.get_all_scraping_urls_by_group(1)
    print(scraping_urls)
    await rep.close()


asyncio.run(main())
