from domain.entities.attack import AttackBody, PartialAttack
from domain.entities.playable_character import (
    PartialPlayableCharacter,
    PlayableCharacterBody,
    PlayableCharacterHead,
)
from domain.entities.spell import PartialSpell, SpellBody
from domain.entities.spell_slot import PartialSpellSlot, SpellSlotBody
from pydantic import Field


class CharacterSheetSpellSlot(SpellSlotBody):
    spells: list[SpellBody] = Field(default=[])


class CharacterSheetBody(PlayableCharacterBody):
    attacks: list[AttackBody] = Field(default=[])
    spell_slots: list[CharacterSheetSpellSlot] = Field(default=[])


class CharacterSheet(PlayableCharacterHead, CharacterSheetBody):
    pass


# ===


class PartialCharacterSheetSpellSlot(PartialSpellSlot):
    spells: list[PartialSpell]


class PartialCharacterSheet(PartialPlayableCharacter):
    attacks: list[PartialAttack]
    spell_slots: list[PartialCharacterSheetSpellSlot]
