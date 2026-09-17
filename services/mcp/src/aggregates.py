from typing import Self

import entities
from asyncpg import Connection


class SpellSlot(entities.SpellSlot):
    spells: list[entities.Spell]


class PlayableCharacter(entities.PlayableCharacter):
    attacks: list[entities.Attack]
    spell_slots: list[SpellSlot]

    @classmethod
    async def get(cls, c: Connection, id: int) -> Self | None:
        pc = cls.model_validate(
            await c.fetchrow(
                """
                SELECT * FROM playable_characters
                WHERE pc_id = $1
                """,
                id,
            )
        )

        if not pc:
            return None

        pc.attacks = [
            entities.Attack.model_validate(attack)
            for attack in await c.fetch(
                """
                SELECT * FROM pc_spells
                WHERE pc_id = $1
                """,
                id,
            )
        ]

        pc.spell_slots = [
            SpellSlot.model_validate(spell_slot)
            for spell_slot in await c.fetch(
                """
                SELECT * FROM pc_spell_slots
                WHERE pc_id = $1
                """,
                id,
            )
        ]

        spells = [
            entities.Spell.model_validate(spell)
            for spell in await c.fetch(
                """
                SELECT * FROM pc_spells
                WHERE pc_id = $1
                """,
                id,
            )
        ]

        for spell in spells:
            pc.spell_slots[spell.level].spells.append(spell)

        return pc
