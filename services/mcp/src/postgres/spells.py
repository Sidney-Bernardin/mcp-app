from asyncpg import Connection

from models.playable_characters import Spell


async def insert_spells(c: Connection, pc_id: int, spells: list[Spell]) -> str:
    return await c.executemany(
        """
        INSERT INTO pc_spells
        VALUES ($1, $2, $3, $4)
        """,
        [(pc_id, spell.name, spell.level, spell.prepared) for spell in spells],
    )
