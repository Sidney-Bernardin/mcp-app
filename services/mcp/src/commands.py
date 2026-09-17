import aggregates
import entities
from pydantic import BaseModel, Field


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


class PlayableCharacterCreation(entities.PlayableCharacterBody):
    attacks: list[entities.Attack]
    spell_slots: list[aggregates.SpellSlot]


class PlayableCharacterUpdate(BaseModel):
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
