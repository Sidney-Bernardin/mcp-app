from pydantic import BaseModel, Field

migration = """
CREATE EXTENTION IF NOT EXISTS hstore;

CREATE TABLE IF NOT EXISTS playable_characters (
    pc_id SERIAL PRIMARY KEY,

    name TEXT NOT NULL,

    stats HSTORE NOT NULL
);
"""


class PCStats(BaseModel):
    level: int = Field(default=1, ge=1)
    race: str
    classs: int = Field(alias="class")
    background: int
    alignment: int

    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    strength_mod: int
    dexterity_mod: int
    constitution_mod: int
    intelligence_mod: int
    wisdom_mod: int
    charisma_mod: int

    strength_sv: int
    dexterity_sv: int
    constitution_sv: int
    intelligence_sv: int
    wisdom_sv: int
    charisma_sv: int

    inspiration: int
    proficiency_bonus: int
    perseption: int

    acrobatics: int
    animal: int
    arcana: int
    athletics: int
    deception: int
    history: int
    insight: int
    intimidation: int
    investigation: int
    medicine: int
    nature: int
    perception: int
    performance: int
    persuasion: int
    religion: int
    sleight_of_hand: int
    stealth: int
    survival: int

    armor_class: int
    initiative: int
    speed: int

    hp_max: int
    hp_current: int
    hp_temp: int

    hit_dice: str
    hit_dice_total: int

    death_saves_successes: int = Field(le=3)
    death_saves_failures: int = Field(le=3)

    copper: int
    silver: int
    emerald: int
    gold: int
    platinum: int
