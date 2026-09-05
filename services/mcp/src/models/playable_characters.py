from pydantic import BaseModel, Field


class Stats(BaseModel):
    level: int = Field(default=1, ge=1)
    xp: int

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

    spell_cast_ability: int
    spell_save_dc: int
    spell_attack_bonus: int


class Attack(BaseModel):
    name: str
    bonus: int
    damage: int
    type: str


class Spell(BaseModel):
    name: str
    level: int
    prepared: bool


class PlayableCharacter(BaseModel):
    pc_id: int

    name: str
    race: str
    classs: str = Field(alias="class")
    spellcasting_class: str
    background: str
    alignment: str

    age: int
    height: int = Field(description="Character height in feet.")
    wight: int = Field(description="Character height in pounds.")
    eyes: str
    skin: str
    hair: str

    stats: Stats
    spell_slot_total: tuple[int, int, int, int, int, int, int, int, int] = Field(
        description="The amount of total spell slots for each level of spell."
    )
    spell_slot_expended: tuple[int, int, int, int, int, int, int, int, int] = Field(
        description="The amount of expended spell slots for each level of spell."
    )

    other_proficiencies_and_languages: list[str] = []
    equipment: list[str] = []
    features_and_traits: list[str] = []

    copper: int
    silver: int
    emerald: int
    gold: int
    platinum: int

    attacks: dict[str, Attack] = {}
    spells: dict[str, Spell] = {}


class UpdateFormStats(BaseModel):
    level: int | None
    xp: int | None

    strength: int | None
    dexterity: int | None
    constitution: int | None
    intelligence: int | None
    wisdom: int | None
    charisma: int | None

    strength_mod: int | None
    dexterity_mod: int | None
    constitution_mod: int | None
    intelligence_mod: int | None
    wisdom_mod: int | None
    charisma_mod: int | None

    strength_sv: int | None
    dexterity_sv: int | None
    constitution_sv: int | None
    intelligence_sv: int | None
    wisdom_sv: int | None
    charisma_sv: int | None

    inspiration: int | None
    proficiency_bonus: int | None
    perseption: int | None

    acrobatics: int | None
    animal: int | None
    arcana: int | None
    athletics: int | None
    deception: int | None
    history: int | None
    insight: int | None
    intimidation: int | None
    investigation: int | None
    medicine: int | None
    nature: int | None
    perception: int | None
    performance: int | None
    persuasion: int | None
    religion: int | None
    sleight_of_hand: int | None
    stealth: int | None
    survival: int | None

    armor_class: int | None
    initiative: int | None
    speed: int | None

    hp_max: int | None
    hp_current: int | None
    hp_temp: int | None

    hit_dice: str | None
    hit_dice_total: int | None

    death_saves_successes: int | None
    death_saves_failures: int | None

    spell_cast_ability: int | None
    spell_save_dc: int | None
    spell_attack_bonus: int | None


class UpdateForm(BaseModel):
    pc_id: int

    name: str | None = None
    race: str | None = None
    classs: str | None = None
    spellcasting_class: str | None = None
    background: str | None = None
    alignment: str | None = None

    age: int | None = None
    height: int | None = None
    wight: int | None = None
    eyes: str | None = None
    skin: str | None = None
    hair: str | None = None

    stats: UpdateFormStats | None = None
    spell_slot_total: tuple[int, int, int, int, int, int, int, int, int] | None = None  # fmt: off
    spell_slot_expended: tuple[int, int, int, int, int, int, int, int, int] | None = None  # fmt: off

    other_proficiencies_and_languages: list[str] | None = None
    equipment: list[str] | None = None
    features_and_traits: list[str] | None = None

    copper: int | None = None
    silver: int | None = None
    emerald: int | None = None
    gold: int | None = None
    platinum: int | None = None

    attacks: dict[str, Attack] | None = None
    spells: dict[str, Spell] | None = None
