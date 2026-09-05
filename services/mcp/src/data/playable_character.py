from pydantic import BaseModel, Field


class PCStats(BaseModel):
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


class PCAttack(BaseModel):
    name: str
    bonus: int
    damage: int
    type: str


class PCSpell(BaseModel):
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

    stats: PCStats
    spell_slot_total: tuple[int, int, int, int, int, int, int, int, int] = Field(
        description="The amount total of each spell slots for each level of spell."
    )
    spell_slot_expended: tuple[int, int, int, int, int, int, int, int, int] = Field(
        description="The amount of expended spell slots for each level of spell."
    )

    other_proficiencies_and_languages: list[str]
    equipment: list[str]
    features_and_traits: list[str]

    copper: int
    silver: int
    emerald: int
    gold: int
    platinum: int

    attacks: list[PCAttack]
    spells: list[PCSpell]
