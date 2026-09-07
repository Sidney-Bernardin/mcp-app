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
    spells: list[Spell]


class PlayableCharacter(BaseModel):
    pc_id: int

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

    attacks: list[Attack]
    spell_slots: list[SpellSlot]


class AttackUpdate(BaseModel):
    name: str | None = None
    bonus: int | None = None
    damage: int | None = None
    type: str | None = None


class SpellSlotUpdate(BaseModel):
    level: str | None = None
    total: str | None = None
    expended: str | None = None


class SpellUpdate(BaseModel):
    name: str | None = None
    level: int | None = None
    prepared: bool | None = None


class UpdateForm(BaseModel):
    name: str | None
    classs: str | None = Field(alias="class", default=None)
    level: str | None = None
    background: str | None = None
    race: str | None = None
    alignment: str | None = None
    xp: str | None = None

    strength: str | None = None
    dexterity: str | None = None
    constitution: str | None = None
    intelligence: str | None = None
    wisdom: str | None = None
    charisma: str | None = None

    strength_mod: str | None = None
    dexterity_mod: str | None = None
    constitution_mod: str | None = None
    intelligence_mod: str | None = None
    wisdom_mod: str | None = None
    charisma_mod: str | None = None

    strength_sv: str | None = None
    dexterity_sv: str | None = None
    constitution_sv: str | None = None
    intelligence_sv: str | None = None
    wisdom_sv: str | None = None
    charisma_sv: str | None = None

    inspiration: str | None = None
    proficiency_bonus: str | None = None
    perseption: str | None = None

    acrobatics: str | None = None
    animal: str | None = None
    arcana: str | None = None
    athletics: str | None = None
    deception: str | None = None
    history: str | None = None
    insight: str | None = None
    intimidation: str | None = None
    investigation: str | None = None
    medicine: str | None = None
    nature: str | None = None
    perception: str | None = None
    performance: str | None = None
    persuasion: str | None = None
    religion: str | None = None
    sleight_of_hand: str | None = None
    stealth: str | None = None
    survival: str | None = None

    armor_class: str | None = None
    initiative: str | None = None
    speed: str | None = None

    hp_max: str | None = None
    hp_current: str | None = None
    hp_temp: str | None = None

    hit_dice: str | None = None
    hit_dice_total: str | None = None

    death_saves_successes: str | None = None
    death_saves_failures: str | None = None

    other_proficiencies_and_languages: list[str] | None = None
    equipment: list[str] | None = None
    features_and_traits: list[str] | None = None

    copper: str | None = None
    silver: str | None = None
    emerald: str | None = None
    gold: str | None = None
    platinum: str | None = None

    age: str | None = None
    height: str | None = None
    wight: str | None = None
    eyes: str | None = None
    skin: str | None = None
    hair: str | None = None

    spellcasting_class: str | None = None
    spell_cast_ability: str | None = None
    spell_save_dc: str | None = None
    spell_attack_bonus: str | None = None
