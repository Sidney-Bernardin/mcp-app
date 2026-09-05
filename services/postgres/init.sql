CREATE EXTENSION IF NOT EXISTS hstore;

CREATE TABLE IF NOT EXISTS playable_characters (
    pc_id SERIAL PRIMARY KEY,

    name TEXT NOT NULL,
    race TEXT NOT NULL,
    class TEXT NOT NULL,
    background TEXT NOT NULL,
    alignment TEXT NOT NULL,

    age TEXT NOT NULL,
    height TEXT NOT NULL,
    wight TEXT NOT NULL,
    eyes TEXT NOT NULL,
    skin TEXT NOT NULL,
    hair TEXT NOT NULL,

    stats HSTORE NOT NULL,
    spell_slot_total INT[] DEFAULT ARRAY[0, 0, 0, 0, 0, 0, 0, 0, 0] NOT NULL CHECK (cardinality(spell_slot_total) = 9),
    spell_slot_expended INT[] DEFAULT ARRAY[0, 0, 0, 0, 0, 0, 0, 0, 0] NOT NULL CHECK (cardinality(spell_slot_expended) = 9),

    other_proficiencies_and_languages TEXT[] NOT NULL,
    equipment TEXT[] NOT NULL,
    features_and_traits TEXT[] NOT NULL,

    copper INT NOT NULL,
    silver INT NOT NULL,
    emerald INT NOT NULL,
    gold INT NOT NULL,
    platinum INT NOT NULL
);

CREATE TABLE IF NOT EXISTS pc_attacks (
    pc_id SERIAL REFERENCES playable_characters(pc_id),

    name TEXT NOT NULL,
    bonus INT NOT NULL,
    damage TEXT NOT NULL,
    type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pc_spells (
    pc_id SERIAL REFERENCES playable_characters(pc_id),

    name TEXT NOT NULL,
    level INT NOT NULL,
    prepared BOOLEAN NOT NULL
);
