import asyncpg


async def get_database_snapshot(c: asyncpg.Connection):
    # fmt: off
    return [
        await c.fetch("""SELECT * FROM playable_characters"""),
        await c.fetch("""SELECT * FROM pc_attacks"""),
        await c.fetch("""SELECT * FROM pc_spell_slots"""),
        await c.fetch("""SELECT * FROM pc_spells"""),
    ]
    # fmt: on
