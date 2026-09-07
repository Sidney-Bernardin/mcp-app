from asyncpg import Connection

from models.playable_characters import PlayableCharacter, UpdateForm
from postgres.utils import insert_placeholders, update_placeholders


async def insert(c: Connection, pc: PlayableCharacter) -> str:
    dump = pc.model_dump()
    return await c.execute(
        f"""
        INSERT INTO playable_characters
        VALUES ({insert_placeholders(dump)})
        """,
        **dump,
    )


async def update(c: Connection, pc_id: int, update: UpdateForm) -> str:
    dump = update.model_dump()
    return await c.execute(
        f"""
        UPDATE playable_characters
        SET {update_placeholders(dump, 1)}
        WHERE pc_id = $1
        """,
        **dump,
    )


async def select_by_id(cls, c: Connection, pc_id: str) -> PlayableCharacter | None:
    return cls.model_validate(
        await c.fetchrow(
            """
            SELECT * FROM playable_characters
            WHERE pc_id = $1
            """,
            pc_id,
        )
    )
