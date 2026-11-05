import aggregates
import asyncpg
import pytest
from commands import PlayableCharacterCreation
from postgres.playable_characters import insert


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


# await insert(pg, fake_playable_character)


# @pytest.mark.asyncio
# async def test_select(pg: asyncpg.Connection):
#     await pg.fetch("SELECT * FROM users")
