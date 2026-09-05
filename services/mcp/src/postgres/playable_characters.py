from typing import Self

from asyncpg import Connection


async def insert(self, c: Connection, attacks: list[Attack], spells: list[Spell]):
    async with c.transaction():
        await c.execute(
            """
            INSERT INTO playable_characters
            VALUES (
                $1,
                $2, $3, $4, $5, $6, $7,
                $8, $9, $10, $11, $12, $13,
                $14, $15, $16,
                $17, $18, $19,
                $20, $21, $22, $23, $24,
            )
            """,
            self.pc_id,
            self.name, self.race, self.classs, self.spellcasting_class, self.background, self.alignment,
            self.age, self.height, self.wight, self.eyes, self.skin, self.hair,
            self.stats, self.spell_slot_total, self.spell_slot_expended,
            self.other_proficiencies_and_languages, self.equipment, self.features_and_traits,
            self.copper, self.silver, self.emerald, self.gold, self.platinum,
        )  # fmt: off

        await c.executemany(
            """
            INSERT INTO pc_attacks
            VALUES ($1, $2, $3, $4)
            """,
            [
                (self.pc_id, attack.name, attack.bonus, attack.damage, attack.type)
                for attack in attacks
            ],
        )

        await c.executemany(
            """
            INSERT INTO pc_spells
            VALUES ($1, $2, $3, $4)
            """,
            [(self.pc_id, spell.name, spell.level, spell.prepared) for spell in spells],
        )


async def update_by_id(
    self, c: Connection, attacks: list[Attack], spells: list[Spell]
) -> str:
    async with c.transaction():
        return await c.execute(
            """
            UPDATE playable_characters
            SET
                name = $2,
                race = $3,
                class = $4,
                spellcasting_class = $5,
                background = $6,
                alignment = $7,

                age = $8,
                height = $9,
                wight = $10,
                eyes = $11,
                skin = $12,
                hair = $13,

                stats = $14,
                spell_slot_total = $15,
                spell_slot_expended = $16,

                other_proficiencies_and_languages = $17,
                equipment = $18,
                features_and_traits = $19,

                copper = $20,
                silver = $21,
                emerald = $22,
                gold = $23,
                platinum = $24,
            WHERE pc_id = $1
            """,
            self.pc_id,
            self.name, self.race, self.classs, self.spellcasting_class, self.background, self.alignment,
            self.age, self.height, self.wight, self.eyes, self.skin, self.hair,
            self.stats, self.spell_slot_total, self.spell_slot_expended,
            self.other_proficiencies_and_languages, self.equipment, self.features_and_traits,
            self.copper, self.silver, self.emerald, self.gold, self.platinum,
        )  # fmt: off

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

        await c.executemany(
            """
            UPDATE pc_spells
            SET
                name = $2
                spell.level = $3
                spell.prepared = $4
            WHERE pc_id = $1 AND name = $2
            """,
            [(self.pc_id, spell.name, spell.level, spell.prepared) for spell in spells],
        )


@classmethod
async def select_by_id(cls, c: Connection, pc_id: str) -> Self | None:
    async with c.transaction():
        pc = cls.model_validate(
            await c.fetchrow(
                """
                SELECT * FROM playable_characters
                WHERE pc_id = $1
                """,
                pc_id,
            )
        )

        for attack in await c.fetch(
            """
            SELECT * FROM pc_attacks
            WHERE pc_id = $1
            """,
            pc_id,
        ):
            attack = Attack.model_validate(attack)
            pc.attacks[attack.name] = attack

        for spell in await c.fetch(
            """
            SELECT * FROM pc_spells
            WHERE pc_id = $1
            """,
            pc_id,
        ):
            spell = Spell.model_validate(spell)
            pc.spells[spell.name] = spell

        return pc
