import aggregates
import asyncpg
import pytest
from commands import PlayableCharacterCreation
from postgres.playable_characters import insert, select_by_id


@pytest.mark.asyncio
async def test_insert(
    pg: asyncpg.Connection, fake_playable_character: aggregates.PlayableCharacter
):
    await insert(
        pg,
        PlayableCharacterCreation.model_validate(
            fake_playable_character.model_dump(), by_name=True
        ),
    )


@pytest.mark.asyncio
async def test_select(
    pg: asyncpg.Connection, fake_playable_character: aggregates.PlayableCharacter
):
    pc = await select_by_id(pg, 1)
    assert pc == fake_playable_character

    pc = await select_by_id(pg, 100)
    assert pc == None
