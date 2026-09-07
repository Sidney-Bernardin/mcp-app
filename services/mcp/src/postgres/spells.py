from asyncpg import Connection

from models.playable_characters import Spell, SpellUpdate


async def insert_rows(c: Connection, pc_id: int, spells: list[Spell]) -> str:
    return await c.executemany(
        """
        INSERT INTO pc_spells
        VALUES ($1, $2, $3, $4)
        """,
        [(pc_id, spell.name, spell.level, spell.prepared) for spell in spells],
    )


async def update_rows(c: Connection, pc_id, updates: list[SpellUpdate]) -> str:
    return await c.executemany(
        """
        UPDATE pc_spells
        SET
            name = $2
            level = $3
            prepared = $4
        WHERE pc_id = $1 AND name = $2
        """,
        [(pc_id, update.name, update.level, update.prepared) for update in updates],
    )


async def select_by_pc_id(cls, c: Connection, pc_id: str) -> list[Spell]:
    return [
        Spell.model_validate(spell)
        for spell in await c.fetch(
            """
            SELECT * FROM pc_spells
            WHERE pc_id = $1
            """,
            pc_id,
        )
    ]
