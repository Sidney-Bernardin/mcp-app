CREATE TABLE IF NOT EXISTS playable_characters (
    pc_id SERIAL PRIMARY KEY,

    name TEXT NOT NULL,
    class TEXT NOT NULL,
    level TEXT NOT NULL,
    background TEXT NOT NULL,
    race TEXT NOT NULL,
    alignment TEXT NOT NULL,
    xp TEXT NOT NULL,

    age TEXT NOT NULL,
    height TEXT NOT NULL,
    wight TEXT NOT NULL,
    eyes TEXT NOT NULL,
    skin TEXT NOT NULL,
    hair TEXT NOT NULL,

    strength TEXT NOT NULL,
    dexterity TEXT NOT NULL,
    constitution TEXT NOT NULL,
    intelligence TEXT NOT NULL,
    wisdom TEXT NOT NULL,
    charisma TEXT NOT NULL,

    strength_mod TEXT NOT NULL,
    dexterity_mod TEXT NOT NULL,
    constitution_mod TEXT NOT NULL,
    intelligence_mod TEXT NOT NULL,
    wisdom_mod TEXT NOT NULL,
    charisma_mod TEXT NOT NULL,

    strength_sv TEXT NOT NULL,
    dexterity_sv TEXT NOT NULL,
    constitution_sv TEXT NOT NULL,
    intelligence_sv TEXT NOT NULL,
    wisdom_sv TEXT NOT NULL,
    charisma_sv TEXT NOT NULL,

    inspiration TEXT NOT NULL,
    proficiency_bonus TEXT NOT NULL,
    perseption TEXT NOT NULL,

    acrobatics TEXT NOT NULL,
    animal TEXT NOT NULL,
    arcana TEXT NOT NULL,
    athletics TEXT NOT NULL,
    deception TEXT NOT NULL,
    history TEXT NOT NULL,
    insight TEXT NOT NULL,
    intimidation TEXT NOT NULL,
    investigation TEXT NOT NULL,
    medicine TEXT NOT NULL,
    nature TEXT NOT NULL,
    perception TEXT NOT NULL,
    performance TEXT NOT NULL,
    persuasion TEXT NOT NULL,
    religion TEXT NOT NULL,
    sleight_of_hand TEXT NOT NULL,
    stealth TEXT NOT NULL,
    survival TEXT NOT NULL,

    armor_class TEXT NOT NULL,
    initiative TEXT NOT NULL,
    speed TEXT NOT NULL,

    hp_max TEXT NOT NULL,
    hp_current TEXT NOT NULL,

    hp_temp TEXT NOT NULL,
    hit_dice TEXT NOT NULL,
    hit_dice_total TEXT NOT NULL,

    death_saves_successes TEXT NOT NULL,
    death_saves_failures TEXT NOT NULL,

    spell_cast_ability TEXT NOT NULL,
    spell_save_dc TEXT NOT NULL,
    spell_attack_bonus TEXT NOT NULL,

    spell_slot_total INT[] DEFAULT ARRAY[0, 0, 0, 0, 0, 0, 0, 0, 0] NOT NULL CHECK (cardinality(spell_slot_total) = 9),
    spell_slot_expended INT[] DEFAULT ARRAY[0, 0, 0, 0, 0, 0, 0, 0, 0] NOT NULL CHECK (cardinality(spell_slot_expended) = 9),

    other_proficiencies_and_languages TEXT[] NOT NULL,
    equipment TEXT[] NOT NULL,
    features_and_traits TEXT[] NOT NULL,

    copper TEXT NOT NULL,
    silver TEXT NOT NULL,
    emerald TEXT NOT NULL,
    gold TEXT NOT NULL,
    platinum TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pc_attacks (
    pc_id SERIAL REFERENCES playable_characters(pc_id),
    name TEXT NOT NULL,

    bonus TEXT NOT NULL,
    damage TEXT NOT NULL,
    type TEXT NOT NULL,

    PRIMARY KEY (pc_id, name)
);

CREATE TABLE IF NOT EXISTS pc_spell_slot (
    pc_id SERIAL REFERENCES playable_characters(pc_id),

    level TEXT NOT NULL,
    total TEXT NOT NULL,
    expended TEXT NOT NULL,

    PRIMARY KEY (pc_id, level)
);

CREATE TABLE IF NOT EXISTS pc_spells (
    pc_id SERIAL REFERENCES playable_characters(pc_id),

    name TEXT NOT NULL,
    level TEXT NOT NULL,
    prepared BOOLEAN NOT NULL
);
