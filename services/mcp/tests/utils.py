import asyncpg
from domain.entities.attack import Attack
from domain.entities.playable_character import PlayableCharacter
from domain.entities.spell import Spell
from domain.entities.spell_slot import SpellSlot


async def get_database_snapshot(c: asyncpg.Connection):
    # fmt: off
    return [
        await c.fetch(c, PlayableCharacter, """SELECT * FROM playable_characters"""), 
        await c.fetch(c, Attack, """SELECT * FROM pc_attacks"""),
        await c.fetch(c, SpellSlot, """SELECT * FROM pc_spell_slots"""),
        await c.fetch(c, Spell, """SELECT * FROM pc_spells"""),
    ]
    # fmt: on
