from asyncpg import Connection
from commands import PlayableCharacterUpdate
from entities import PlayableCharacter
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


async def update(c: Connection, pc_id: int, update: PlayableCharacterUpdate) -> str:
    dump = update.model_dump()
    return await c.execute(
        f"""
        UPDATE playable_characters
        SET {update_placeholders(dump, 1)}
        WHERE pc_id = $1
        """,
        **dump,
    )


async def select_by_id(c: Connection, pc_id: int) -> PlayableCharacter | None:
    return PlayableCharacter.model_validate(
        await c.fetchrow(
            """
            SELECT * FROM playable_characters
            WHERE pc_id = $1
            """,
            pc_id,
        )
    )
