import asyncpg
import pytest
from domain.entities.attack import Attack, AttackBody, PartialAttack
from domain.entities.playable_character import (
    PartialPlayableCharacter,
    PlayableCharacter,
    PlayableCharacterBody,
)
from domain.entities.spell import PartialSpell, Spell, SpellBody
from domain.entities.spell_slot import PartialSpellSlot, SpellSlot, SpellSlotBody
from domain.repositories.postgres.queries import (
    pc_attacks,
    pc_spell_slots,
    pc_spells,
    playable_characters,
)
from domain.repositories.postgres.utils import fetch
from utils import get_database_snapshot

# fmt: off
fake_playable_character = PlayableCharacter(
    id = 2,

    name = "",
    **{"class": ""},
    level = 0,
    background = "",
    race = "",
    alignment = "",
    xp = "",

    strength = "",
    dexterity = "",
    constitution = "",
    intelligence = "",
    wisdom = "",
    charisma = "",

    strength_mod = "",
    dexterity_mod = "",
    constitution_mod = "",
    intelligence_mod = "",
    wisdom_mod = "",
    charisma_mod = "",

    strength_sv = "",
    dexterity_sv = "",
    constitution_sv = "",
    intelligence_sv = "",
    wisdom_sv = "",
    charisma_sv = "",

    inspiration = "",
    proficiency_bonus = "",
    perseption = "",

    acrobatics = "",
    animal = "",
    arcana = "",
    athletics = "",
    deception = "",
    history = "",
    insight = "",
    intimidation = "",
    investigation = "",
    medicine = "",
    nature = "",
    perception = "",
    performance = "",
    persuasion = "",
    religion = "",
    sleight_of_hand = "",
    stealth = "",
    survival = "",

    armor_class = "",
    initiative = "",
    speed = "",

    hp_max = "",
    hp_current = "",
    hp_temp = "",

    hit_dice = "",
    hit_dice_total = "",

    death_saves_successes = "",
    death_saves_failures = "",

    other_proficiencies_and_languages = [],
    equipment = [],
    features_and_traits = [],

    copper = "",
    silver = "",
    emerald = "",
    gold = "",
    platinum = "",

    age = "",
    height = "",
    wight = "",
    eyes = "",
    skin = "",
    hair = "",

    spell_cast_class = "",
    spell_cast_ability = "",
    spell_save_dc = "",
    spell_attack_bonus = "",
)

fake_attack = Attack(
    pc_id = 2,

    name = "",
    bonus = "",
    damage = "",
    type = "",
)

fake_spell_slot = SpellSlot(
    pc_id = 2,

    level = 0,
    total = "",
    expended = "",
)

fake_spell = Spell(
    pc_id = 2,

    name = "",
    level = 0,
    prepared = False,
)
# fmt: on


@pytest.mark.asyncio
async def test_writes(pg: asyncpg.Connection, snapshot):
    # fmt: off
    tests = [
        (playable_characters.INSERT,
            PlayableCharacterBody.model_validate(fake_playable_character.model_dump()).model_dump().values()),
        (pc_attacks.INSERT,
            fake_attack.model_dump().values()),
        (pc_spell_slots.INSERT,
            fake_spell_slot.model_dump().values()),
        (pc_spells.INSERT,
            fake_spell.model_dump().values()),

        (playable_characters.UPDATE,
            (1, *PartialPlayableCharacter.model_validate(fake_playable_character.model_dump()).model_dump().values())),
        (pc_attacks.UPDATE,
            (1, *PartialAttack.model_validate(fake_attack.model_dump()).model_dump().values())),
        (pc_spell_slots.UPDATE,
            (1, *PartialSpellSlot.model_validate(fake_spell_slot.model_dump()).model_dump().values())),
        (pc_spells.UPDATE,
            (1, *PartialSpell.model_validate(fake_spell.model_dump()).model_dump().values())),
    ]
    # fmt: on

    for query, args in tests:
        await pg.execute(query, *args)

    assert snapshot == get_database_snapshot(pg)


@pytest.mark.asyncio
async def test_reads(pg: asyncpg.Connection, snapshot):
    tests = [
        (PlayableCharacter, playable_characters.SELECT, (1,)),
        (PlayableCharacter, playable_characters.SELECT, (100,)),
        (Attack, pc_attacks.SELECT, (1,)),
        (Attack, pc_attacks.SELECT, (100,)),
        (SpellSlot, pc_spell_slots.SELECT, (1,)),
        (SpellSlot, pc_spell_slots.SELECT, (100,)),
        (Spell, pc_spells.SELECT, (1,)),
        (Spell, pc_spells.SELECT, (100,)),
    ]

    assert snapshot == [
        await fetch(pg, model, query, *args) for model, query, args in tests
    ]
