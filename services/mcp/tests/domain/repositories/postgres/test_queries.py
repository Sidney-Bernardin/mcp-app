import asyncpg
import pytest
from domain.entities.attack import Attack, PartialAttack
from domain.entities.playable_character import (
    PartialPlayableCharacter,
    PlayableCharacter,
    PlayableCharacterBody,
)
from domain.entities.spell import PartialSpell, Spell
from domain.entities.spell_slot import PartialSpellSlot, SpellSlot
from domain.entities.test_attack import fake_attack
from domain.entities.test_playable_character import fake_playable_character
from domain.entities.test_spell import fake_spell
from domain.entities.test_spell_slot import fake_spell_slot
from domain.repositories.postgres.queries import (
    pc_attacks,
    pc_spell_slots,
    pc_spells,
    playable_characters,
)
from domain.repositories.postgres.utils import fetch
from utils import get_database_snapshot


@pytest.mark.asyncio
async def test_writes(subtests: pytest.Subtests, snapshot, pg: asyncpg.Connection):
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
        with subtests.test(msg=query, args=args):
            await pg.execute(query, *args)
            assert snapshot == await get_database_snapshot(pg)


@pytest.mark.asyncio
async def test_reads(subtests: pytest.Subtests, snapshot, pg: asyncpg.Connection):
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

    for model, query, args in tests:
        with subtests.test(msg=query, args=args):
            assert snapshot == await fetch(pg, model, query, *args)
