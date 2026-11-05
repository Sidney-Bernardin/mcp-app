INSERT INTO "playable_characters" (
	"name", "class", "level", "background", "race", "alignment", "xp",
	"age", "height", "wight", "eyes", "skin", "hair",
	"strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma",
	"strength_mod", "dexterity_mod", "constitution_mod", "intelligence_mod", "wisdom_mod", "charisma_mod",
	"strength_sv", "dexterity_sv", "constitution_sv", "intelligence_sv", "wisdom_sv", "charisma_sv",
	"inspiration", "proficiency_bonus", "perseption", "acrobatics", "animal", "arcana", "athletics",
	"deception", "history", "insight", "intimidation", "investigation", "medicine", "nature",
	"perception", "performance", "persuasion", "religion", "sleight_of_hand", "stealth", "survival",
	"armor_class", "initiative", "speed", "hp_max", "hp_current", "hp_temp", "hit_dice", "hit_dice_total",
	"death_saves_successes", "death_saves_failures", "spell_cast_class", "spell_cast_ability", "spell_save_dc", "spell_attack_bonus",
	"other_proficiencies_and_languages", "equipment", "features_and_traits",
	"copper", "silver", "emerald", "gold", "platinum"
) VALUES
(
	'', '', 0, '', '', '', '', '', '', '',
	'', '', '', '', '', '', '', '', '', '',
	'', '', '', '', '', '', '', '', '', '',
	'', '', '', '', '', '', '', '', '', '',
	'', '', '', '', '', '', '', '', '', '',
	'', '', '', '', '', '', '', '', '', '',
	'', '', '', '', '', '',
	'{}', '{}', '{}',
	'', '', '', '', ''
);

INSERT INTO "pc_attacks" ("pc_id", "name", "bonus", "damage", "type") VALUES
(1, '', '', '', '');

INSERT INTO "pc_spell_slots" ("pc_id", "level", "total", "expended") VALUES
(1, 0, '0', '0');

INSERT INTO "pc_spells" ("pc_id", "name", "level", "prepared") VALUES
(1, '', 0, false);

INSERT INTO "users" ("username", "password_hash", "password_halt") VALUES
('1', ''::bytea, ''::bytea);
