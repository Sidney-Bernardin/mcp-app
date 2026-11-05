import entities
from pydantic import Field


class SpellSlot(entities.SpellSlot):
    spells: list[entities.Spell] = Field(default=[])


class PlayableCharacter(entities.PlayableCharacter):
    attacks: list[entities.Attack] = Field(default=[])
    spell_slots: list[SpellSlot] = Field(default=[])
