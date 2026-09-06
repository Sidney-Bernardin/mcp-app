from asyncpg import Connection

from models.playable_characters import Attack, UpdateForm


async def insert_attacks(c: Connection, pc_id: int, attacks: list[Attack]) -> str:
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


async def update(c: Connection, pc_id: int, form: UpdateForm) -> str:
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
            (self.pc_id, attack.name, attack.bonus, attack.damage, attack.type)
            for attack in attacks
        ],
    )
