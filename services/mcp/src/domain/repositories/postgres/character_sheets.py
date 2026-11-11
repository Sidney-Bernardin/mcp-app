from asyncpg import Connection
from domain.aggregates import (
    CharacterSheet,
    CharacterSheetBody,
    CharacterSheetSpellSlot,
    PartialCharacterSheet,
)
from domain.entities.attack import Attack
from domain.entities.playable_character import PlayableCharacter
from domain.entities.spell import Spell, SpellBody
from domain.entities.spell_slot import SpellSlot
from domain.repositories.postgres.queries import (
    pc_attacks,
    pc_spell_slots,
    pc_spells,
    playable_characters,
)
from domain.repositories.postgres.utils import fetch, fetchrow


async def insert(c: Connection, character_sheet: CharacterSheetBody) -> int:
    pc_id = await c.fetchval(
        playable_characters.INSERT,
        *character_sheet.model_dump(exclude={"attacks", "spell_slots"}).values(),
    )

    if not pc_id:
        raise Exception("Cannot insert")

    await c.executemany(
        pc_attacks.INSERT,
        [(*attack.model_dump().values(), pc_id) for attack in character_sheet.attacks],
    )

    await c.executemany(
        pc_spell_slots.INSERT,
        [
            (*spell_slot.model_dump(exclude={"spells"}).values(), pc_id)
            for spell_slot in character_sheet.spell_slots
        ],
    )

    await c.executemany(
        pc_spells.INSERT,
        [
            (*spell.model_dump().values(), pc_id)
            for spell_slot in character_sheet.spell_slots
            for spell in spell_slot.spells
        ],
    )

    return pc_id


async def select(c: Connection, pc_id: int) -> CharacterSheet | None:
    pc = await fetchrow(c, CharacterSheet, playable_characters.SELECT, pc_id)
    if not pc:
        return

    pc.attacks = await fetch(c, Attack, pc_attacks.SELECT, pc_id)
    pc.spell_slots = await fetch(
        c, CharacterSheetSpellSlot, pc_spell_slots.SELECT, pc_id
    )
    spells = await fetch(c, SpellBody, pc_spells.SELECT, pc_id)

    for i, spell in enumerate(spells):
        pc.spell_slots[i].spells.append(spell)

    return pc


async def update(
    c: Connection, pc_id: int, character_sheet: PartialCharacterSheet
) -> None:
    await c.execute(
        playable_characters.UPDATE,
        pc_id,
        *character_sheet.model_dump(exclude={"attacks", "spell_slots"}).values(),
    )

    if character_sheet.attacks:
        await c.executemany(
            pc_attacks.UPDATE,
            [
                (pc_id, *attack.model_dump().values())
                for attack in character_sheet.attacks
            ],
        )

    if character_sheet.spell_slots:
        await c.executemany(
            pc_spell_slots.UPDATE,
            [
                (pc_id, *spell_slot.model_dump(exclude={"spells"}).values())
                for spell_slot in character_sheet.spell_slots
                if character_sheet.spell_slots
            ],
        )

        await c.executemany(
            pc_spells.UPDATE,
            [
                (pc_id, *spell.model_dump().values())
                for spell_slot in character_sheet.spell_slots
                if spell_slot.spells
                for spell in spell_slot.spells
            ],
        )
