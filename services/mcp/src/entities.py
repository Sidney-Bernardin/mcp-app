from pydantic import BaseModel, Field


class Attack(BaseModel):
    name: str
    bonus: int
    damage: int
    type: str


class Spell(BaseModel):
    name: str
    level: int
    prepared: bool


class SpellSlot(BaseModel):
    level: str
    total: str
    expended: str


class PlayableCharacterID(BaseModel):
    id: int


class PlayableCharacterBody(BaseModel):
    name: str
    classs: str = Field(alias="class")
    level: str
    background: str
    race: str
    alignment: str
    xp: str

    strength: str
    dexterity: str
    constitution: str
    intelligence: str
    wisdom: str
    charisma: str

    strength_mod: str
    dexterity_mod: str
    constitution_mod: str
    intelligence_mod: str
    wisdom_mod: str
    charisma_mod: str

    strength_sv: str
    dexterity_sv: str
    constitution_sv: str
    intelligence_sv: str
    wisdom_sv: str
    charisma_sv: str

    inspiration: str
    proficiency_bonus: str
    perseption: str

    acrobatics: str
    animal: str
    arcana: str
    athletics: str
    deception: str
    history: str
    insight: str
    intimidation: str
    investigation: str
    medicine: str
    nature: str
    perception: str
    performance: str
    persuasion: str
    religion: str
    sleight_of_hand: str
    stealth: str
    survival: str

    armor_class: str
    initiative: str
    speed: str

    hp_max: str
    hp_current: str
    hp_temp: str

    hit_dice: str
    hit_dice_total: str

    death_saves_successes: str
    death_saves_failures: str

    other_proficiencies_and_languages: list[str]
    equipment: list[str]
    features_and_traits: list[str]

    copper: str
    silver: str
    emerald: str
    gold: str
    platinum: str

    age: str
    height: str
    wight: str
    eyes: str
    skin: str
    hair: str

    spellcasting_class: str
    spell_cast_ability: str
    spell_save_dc: str
    spell_attack_bonus: str


class PlayableCharacter(PlayableCharacterID, PlayableCharacterBody):
    pass
