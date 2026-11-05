from aggregates import PlayableCharacter, SpellSlot
from asyncpg import Connection
from commands import PlayableCharacterCreation, PlayableCharacterUpdate
from entities import Attack, Spell
from postgres.utils import insert_fields, insert_placeholders, update_placeholders


async def insert(c: Connection, pc: PlayableCharacterCreation) -> None:
    dump = pc.model_dump(exclude={"attacks", "spell_slots"}, by_alias=True)
    pc_id = await c.fetchval(
        f"""
        INSERT INTO playable_characters
        ({insert_fields(dump)})
        VALUES ({insert_placeholders(dump)})
        RETURNING id
        """,
        # **dump,
        *dump.values(),
    )

    await c.executemany(
        """
        INSERT INTO pc_attacks
        VALUES ($1, $2, $3, $4, $5)
        """,
        [
            (pc_id, attack.name, attack.bonus, attack.damage, attack.type)
            for attack in pc.attacks
        ],
    )

    await c.executemany(
        """
        INSERT INTO pc_spell_slots
        VALUES ($1, $2, $3, $4)
        """,
        [
            (
                pc_id,
                spell_slot.level,
                spell_slot.total,
                spell_slot.expended,
            )
            for spell_slot in pc.spell_slots
        ],
    )

    return await c.executemany(
        """
        INSERT INTO pc_spells
        VALUES ($1, $2, $3, $4)
        """,
        [
            (pc_id, spell.name, spell.level, spell.prepared)
            for spell_slot in pc.spell_slots
            for spell in spell_slot.spells
        ],
    )


async def select_by_id(c: Connection, pc_id: int) -> PlayableCharacter | None:

    pc = PlayableCharacter.model_validate(
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
        Attack.model_validate(attack)
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
        Spell.model_validate(spell)
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


async def update(c: Connection, pc_id: int, update: PlayableCharacterUpdate) -> None:
    dump = update.model_dump(exclude={"attacks", "spell_slots"})
    await c.execute(
        f"""
        UPDATE playable_characters
        SET {update_placeholders(dump, 1)}
        WHERE pc_id = $1
        """,
        **dump,
    )

    await c.executemany(
        """
        UPDATE pc_attacks
        SET
            name = $2,
            bonus = $3,
            damage = $4,
            type = $5
        WHERE pc_id = $1 AND name = $2
        """,
        [
            (pc_id, update.name, update.bonus, update.damage, update.type)
            for update in update.attacks
        ],
    )

    await c.executemany(
        """
        UPDATE pc_spell_slots
        SET
            level = $2,
            total = $3,
            expended = $4,
        WHERE pc_id = $1 AND level = $2
        """,
        [
            (pc_id, update.level, update.total, update.expended)
            for update in update.spell_slots
        ],
    )

    await c.executemany(
        """
        UPDATE pc_spells
        SET
            name = $2
            level = $3
            prepared = $4
        WHERE pc_id = $1 AND name = $2
        """,
        [
            (pc_id, update.name, update.level, update.prepared)
            for spell_slot_update in update.spell_slots
            for update in spell_slot_update.spells
        ],
    )
