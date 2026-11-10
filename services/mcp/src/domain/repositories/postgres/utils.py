from typing import Any

from asyncpg import Connection


async def fetchrow(c: Connection, model: type, query: str, *args) -> Any | None:
    r = await c.fetchrow(query, *args)
    return model(**dict(r)) if r else None


async def fetch(c: Connection, model: type, query: str, *args) -> list[Any]:
    rr = await c.fetch(query, *args)
    return [model(**dict(r)) for r in rr]
