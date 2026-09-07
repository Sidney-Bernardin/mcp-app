from asyncpg import Connection

from models.playable_characters import SpellSlot, SpellSlotUpdate


async def insert_rows(c: Connection, pc_id: int, spell_slots: list[SpellSlot]) -> str:
    return await c.executemany(
        """
        INSERT INTO pc_spell_slots
        VALUES ($1, $2, $3)
        """,
        [
            (
                pc_id,
                spell_slot.level,
                spell_slot.total,
                spell_slot.expended,
            )
            for spell_slot in spell_slots
        ],
    )


async def update_rows(c: Connection, pc_id: int, updates: list[SpellSlotUpdate]) -> str:
    return await c.executemany(
        """
        UPDATE pc_spell_slots
        SET
            level = $2,
            total = $3,
            expended = $4,
        WHERE pc_id = $1 AND level = $2
        """,
        [(pc_id, update.level, update.total, update.expended) for update in updates],
    )


async def select_by_pc_id(cls, c: Connection, pc_id: str) -> list[SpellSlot]:
    return [
        SpellSlot.model_validate(spell_slot)
        for spell_slot in await c.fetch(
            """
            SELECT * FROM pc_spell_slots
            WHERE pc_id = $1
            """,
            pc_id,
        )
    ]
