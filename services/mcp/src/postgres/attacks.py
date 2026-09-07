from asyncpg import Connection

from models.playable_characters import Attack, AttackUpdate


async def insert_rows(c: Connection, pc_id: int, attacks: list[Attack]) -> str:
    return await c.executemany(
        """
        INSERT INTO pc_attacks
        VALUES ($1, $2, $3, $4)
        """,
        [
            (pc_id, attack.name, attack.bonus, attack.damage, attack.type)
            for attack in attacks
        ],
    )


async def update_rows(c: Connection, pc_id: int, updates: list[AttackUpdate]) -> str:
    return await c.executemany(
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
            for update in updates
        ],
    )


async def select_by_pc_id(cls, c: Connection, pc_id: str) -> list[Attack]:
    return [
        Attack.model_validate(attack)
        for attack in await c.fetch(
            """
            SELECT * FROM pc_spells
            WHERE pc_id = $1
            """,
            pc_id,
        )
    ]
