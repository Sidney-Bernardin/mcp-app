CREATE TABLE "pc_attacks" (
	"pc_id" bigint,
	"name" text,
	"bonus" text NOT NULL,
	"damage" text NOT NULL,
	"type" text NOT NULL,
	CONSTRAINT "pc_attacks_pkey" PRIMARY KEY("pc_id","name")
);
--> statement-breakpoint
CREATE TABLE "pc_spell_slots" (
	"pc_id" bigint,
	"level" integer,
	"total" text NOT NULL,
	"expended" text NOT NULL,
	CONSTRAINT "pc_spell_slots_pkey" PRIMARY KEY("pc_id","level")
);
--> statement-breakpoint
CREATE TABLE "pc_spells" (
	"pc_id" bigint,
	"name" text NOT NULL,
	"level" integer,
	"prepared" boolean NOT NULL,
	CONSTRAINT "pc_spells_pkey" PRIMARY KEY("pc_id","level")
);
--> statement-breakpoint
CREATE TABLE "playable_characters" (
	"id" bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY (sequence name "playable_characters_id_seq" INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START WITH 1 CACHE 1),
	"name" text NOT NULL,
	"class" text NOT NULL,
	"level" integer NOT NULL,
	"background" text NOT NULL,
	"race" text NOT NULL,
	"alignment" text NOT NULL,
	"xp" text NOT NULL,
	"age" text NOT NULL,
	"height" text NOT NULL,
	"wight" text NOT NULL,
	"eyes" text NOT NULL,
	"skin" text NOT NULL,
	"hair" text NOT NULL,
	"strength" text NOT NULL,
	"dexterity" text NOT NULL,
	"constitution" text NOT NULL,
	"intelligence" text NOT NULL,
	"wisdom" text NOT NULL,
	"charisma" text NOT NULL,
	"strength_mod" text NOT NULL,
	"dexterity_mod" text NOT NULL,
	"constitution_mod" text NOT NULL,
	"intelligence_mod" text NOT NULL,
	"wisdom_mod" text NOT NULL,
	"charisma_mod" text NOT NULL,
	"strength_sv" text NOT NULL,
	"dexterity_sv" text NOT NULL,
	"constitution_sv" text NOT NULL,
	"intelligence_sv" text NOT NULL,
	"wisdom_sv" text NOT NULL,
	"charisma_sv" text NOT NULL,
	"inspiration" text NOT NULL,
	"proficiency_bonus" text NOT NULL,
	"perseption" text NOT NULL,
	"acrobatics" text NOT NULL,
	"animal" text NOT NULL,
	"arcana" text NOT NULL,
	"athletics" text NOT NULL,
	"deception" text NOT NULL,
	"history" text NOT NULL,
	"insight" text NOT NULL,
	"intimidation" text NOT NULL,
	"investigation" text NOT NULL,
	"medicine" text NOT NULL,
	"nature" text NOT NULL,
	"perception" text NOT NULL,
	"performance" text NOT NULL,
	"persuasion" text NOT NULL,
	"religion" text NOT NULL,
	"sleight_of_hand" text NOT NULL,
	"stealth" text NOT NULL,
	"survival" text NOT NULL,
	"armor_class" text NOT NULL,
	"initiative" text NOT NULL,
	"speed" text NOT NULL,
	"hp_max" text NOT NULL,
	"hp_current" text NOT NULL,
	"hp_temp" text NOT NULL,
	"hit_dice" text NOT NULL,
	"hit_dice_total" text NOT NULL,
	"death_saves_successes" text NOT NULL,
	"death_saves_failures" text NOT NULL,
	"spell_cast_class" text NOT NULL,
	"spell_cast_ability" text NOT NULL,
	"spell_save_dc" text NOT NULL,
	"spell_attack_bonus" text NOT NULL,
	"spell_slot_total" integer[] DEFAULT ARRAY[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]::integer[],
	"spell_slot_expended" integer[] DEFAULT ARRAY[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]::integer[],
	"other_proficiencies_and_languages" text[] NOT NULL,
	"equipment" text[] NOT NULL,
	"features_and_traits" text[] NOT NULL,
	"copper" text NOT NULL,
	"silver" text NOT NULL,
	"emerald" text NOT NULL,
	"gold" text NOT NULL,
	"platinum" text NOT NULL,
	CONSTRAINT "spell_slot_total_check" CHECK (cardinality("spell_slot_total") = 10),
	CONSTRAINT "spell_slot_expended_check" CHECK (cardinality("spell_slot_expended") = 10)
);
--> statement-breakpoint
CREATE TABLE "users" (
	"id" bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY (sequence name "users_id_seq" INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START WITH 1 CACHE 1),
	"username" varchar(255) NOT NULL UNIQUE,
	"password_hash" bytea NOT NULL,
	"password_halt" bytea NOT NULL,
	"created_at" timestamp DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE INDEX "username" ON "users" ("username");--> statement-breakpoint
ALTER TABLE "pc_attacks" ADD CONSTRAINT "pc_attacks_pc_id_playable_characters_id_fkey" FOREIGN KEY ("pc_id") REFERENCES "playable_characters"("id");--> statement-breakpoint
ALTER TABLE "pc_spell_slots" ADD CONSTRAINT "pc_spell_slots_pc_id_playable_characters_id_fkey" FOREIGN KEY ("pc_id") REFERENCES "playable_characters"("id");--> statement-breakpoint
ALTER TABLE "pc_spells" ADD CONSTRAINT "pc_spells_pc_id_level_pc_spell_slots_pc_id_level_fkey" FOREIGN KEY ("pc_id","level") REFERENCES "pc_spell_slots"("pc_id","level");