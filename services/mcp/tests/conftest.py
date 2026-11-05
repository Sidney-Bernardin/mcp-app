from pathlib import Path
from urllib.parse import urlsplit

import aggregates
import asyncpg
import config
import entities
import pytest_asyncio

migrations: list[str] | None = None


@pytest_asyncio.fixture
async def pg():
    global migrations

    url = urlsplit(config.PG_URL)
    conn: asyncpg.Connection = await asyncpg.connect(
        host=url.hostname,
        port=url.port,
        user=url.username,
        password=url.password,
        database="postgres",
    )

    await conn.execute("DROP DATABASE IF EXISTS test")
    await conn.execute("CREATE DATABASE test")
    await conn.close()

    conn: asyncpg.Connection = await asyncpg.connect(
        host=url.hostname,
        port=url.port,
        user=url.username,
        password=url.password,
        database="test",
    )

    if not migrations:
        parent_dir = Path(__file__).resolve().parent
        migration_dir = parent_dir / "../../postgres/migrations"
        test_data_file = parent_dir / "../../postgres/test_data.sql"

        migration_files = sorted(
            [p / "migration.sql" for p in migration_dir.iterdir() if p.is_dir()],
            key=lambda p: p.stat().st_mtime,
        )

        migrations = [m.read_text() for m in migration_files]
        migrations.append(test_data_file.read_text())

    for m in migrations:
        await conn.execute(m)

    yield conn

    await conn.close()


@pytest_asyncio.fixture
async def fake_playable_character(pg: asyncpg.Connection):

    pc = aggregates.PlayableCharacter.model_validate(
        dict(await pg.fetchrow("""SELECT * FROM playable_characters WHERE id = '1'""")),
    )

    pc.attacks = [
        entities.Attack.model_validate(dict(row))
        for row in await pg.fetch("""SELECT * FROM pc_attacks WHERE pc_id = '1'""")
    ]

    pc.spell_slots = [
        aggregates.SpellSlot.model_validate(dict(row))
        for row in await pg.fetch("""SELECT * FROM pc_spell_slots WHERE pc_id = '1'""")
    ]

    spells = [
        entities.Spell.model_validate(dict(row))
        for row in await pg.fetch("""SELECT * FROM pc_spells WHERE pc_id = '1'""")
    ]

    for spell in spells:
        pc.spell_slots[spell.level].spells.append(spell)

    yield pc
