from typing import Any

from asyncpg import Connection


def insert_placeholders(d: dict[str, Any]) -> str:
    return ", ".join([f"${i + 1}" for i in range(len(d))])


def insert_fields(d: dict[str, Any]) -> str:
    return ", ".join(d.keys())


def update_placeholders(d: dict[str, Any], base: int) -> str:
    return ", ".join(
        [f"{key} = COALESCE(${base + i + 1}, {key})" for i, key in enumerate(d)]
    )


async def fetchrow(c: Connection, view: type, query: str, *args) -> Any | None:
    r = await c.fetchrow(query, *args)
    return view(**dict(r)) if r else None


async def fetch(c: Connection, view: type, query: str, *args) -> list[Any]:
    rr = await c.fetch(query, *args)
    return [view(**dict(r)) for r in rr]
