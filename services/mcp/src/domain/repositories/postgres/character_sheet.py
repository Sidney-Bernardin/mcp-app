from asyncpg import Connection
from domain.aggregates import PartialCharacterSheet
from domain.repositories.postgres.queries import (
    pc_attacks,
    pc_spell_slots,
    pc_spells,
    playable_characters,
)


async def update(c: Connection, pc_id: int, character_sheet: PartialCharacterSheet):
    await c.execute(
        playable_characters.UPDATE,
        pc_id,
        *character_sheet.model_dump(exclude={"attacks", "spell_slots"}).values(),
    )

    await c.executemany(
        pc_attacks.UPDATE,
        [(pc_id, *attack.model_dump().values()) for attack in character_sheet.attacks],
    )

    await c.executemany(
        pc_spell_slots.UPDATE,
        [
            (pc_id, *spell_slot.model_dump().values())
            for spell_slot in character_sheet.spell_slots
        ],
    )

    await c.executemany(
        pc_spells.UPDATE,
        [
            (pc_id, *spell.model_dump().values())
            for spell_slot in character_sheet.spell_slots
            for spell in spell_slot.spells
        ],
    )
