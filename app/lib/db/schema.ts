"server only"

import { sql } from "drizzle-orm"
import { defineRelations } from "drizzle-orm"
import {
  pgTable, primaryKey, check, foreignKey,
  bytea, text, serial, varchar, integer, boolean, timestamp,
  index,
  bigint,
} from "drizzle-orm/pg-core"
import { NodePgDatabase, NodePgTransaction } from "drizzle-orm/node-postgres"


export type DB =
  | NodePgDatabase<typeof relations>
  | NodePgTransaction<typeof relations>


export const users = pgTable("users", {
  id: bigint({ mode: "bigint" }).generatedAlwaysAsIdentity().primaryKey(),
  username: varchar({ length: 255 }).notNull().unique(),
  password_hash: bytea().notNull(),
  password_halt: bytea().notNull(),
  created_at: timestamp().defaultNow().notNull(),
}, (table) => ([
  index("username").on(table.username)
]))


export const playableCharacters = pgTable("playable_characters", {
  id: bigint({ mode: "bigint" }).generatedAlwaysAsIdentity().primaryKey(),

  name: text().notNull(),
  class: text().notNull(),
  level: integer().notNull(),
  background: text().notNull(),
  race: text().notNull(),
  alignment: text().notNull(),
  xp: text().notNull(),

  age: text().notNull(),
  height: text().notNull(),
  wight: text().notNull(),
  eyes: text().notNull(),
  skin: text().notNull(),
  hair: text().notNull(),

  strength: text().notNull(),
  dexterity: text().notNull(),
  constitution: text().notNull(),
  intelligence: text().notNull(),
  wisdom: text().notNull(),
  charisma: text().notNull(),

  strength_mod: text().notNull(),
  dexterity_mod: text().notNull(),
  constitution_mod: text().notNull(),
  intelligence_mod: text().notNull(),
  wisdom_mod: text().notNull(),
  charisma_mod: text().notNull(),

  strength_sv: text().notNull(),
  dexterity_sv: text().notNull(),
  constitution_sv: text().notNull(),
  intelligence_sv: text().notNull(),
  wisdom_sv: text().notNull(),
  charisma_sv: text().notNull(),

  inspiration: text().notNull(),
  proficiency_bonus: text().notNull(),
  perseption: text().notNull(),

  acrobatics: text().notNull(),
  animal: text().notNull(),
  arcana: text().notNull(),
  athletics: text().notNull(),
  deception: text().notNull(),
  history: text().notNull(),
  insight: text().notNull(),
  intimidation: text().notNull(),
  investigation: text().notNull(),
  medicine: text().notNull(),
  nature: text().notNull(),
  perception: text().notNull(),
  performance: text().notNull(),
  persuasion: text().notNull(),
  religion: text().notNull(),
  sleight_of_hand: text().notNull(),
  stealth: text().notNull(),
  survival: text().notNull(),

  armor_class: text().notNull(),
  initiative: text().notNull(),
  speed: text().notNull(),

  hp_max: text().notNull(),
  hp_current: text().notNull(),

  hp_temp: text().notNull(),
  hit_dice: text().notNull(),
  hit_dice_total: text().notNull(),

  death_saves_successes: text().notNull(),
  death_saves_failures: text().notNull(),

  spell_cast_class: text().notNull(),
  spell_cast_ability: text().notNull(),
  spell_save_dc: text().notNull(),
  spell_attack_bonus: text().notNull(),

  spell_slot_total: integer().array().default(sql`ARRAY[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`),
  spell_slot_expended: integer().array().default(sql`ARRAY[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`),

  other_proficiencies_and_languages: text().array().notNull(),
  equipment: text().array().notNull(),
  features_and_traits: text().array().notNull(),

  copper: text().notNull(),
  silver: text().notNull(),
  emerald: text().notNull(),
  gold: text().notNull(),
  platinum: text().notNull(),
}, (table) => [
  check("spell_slot_total_check", sql`cardinality(${table.spell_slot_total}) = 10`),
  check("spell_slot_expended_check", sql`cardinality(${table.spell_slot_expended}) = 10`),
])


export const pcAttacks = pgTable("pc_attacks", {
  pc_id: bigint({ mode: "bigint" }).references(() => playableCharacters.id),
  name: text().notNull(),

  bonus: text().notNull(),
  damage: text().notNull(),
  type: text().notNull(),
}, (table) => [
  primaryKey({ columns: [table.pc_id, table.name] }),
])


export const pcSpellSlots = pgTable("pc_spell_slots", {
  pc_id: bigint({ mode: "bigint" }).notNull().references(() => playableCharacters.id),
  level: integer().notNull(),

  total: text().notNull(),
  expended: text().notNull(),
}, (table) => [
  primaryKey({ columns: [table.pc_id, table.level] }),
])


export const pcSpells = pgTable("pc_spells", {
  pc_id: bigint({ mode: "bigint" }),
  name: text().notNull(),

  level: integer().notNull(),
  prepared: boolean().notNull(),
}, (table) => [
  primaryKey({ columns: [table.pc_id, table.level] }),
  foreignKey({
    columns: [table.pc_id, table.level],
    foreignColumns: [pcSpellSlots.pc_id, pcSpellSlots.level],
  }),
])


export const relations = defineRelations({ users, playableCharacters, pcAttacks, pcSpellSlots, pcSpells }, (r) => ({
  playableCharacters: {
    pcAttacks: r.many.pcAttacks({
      from: r.playableCharacters.id,
      to: r.pcAttacks.pc_id,
    }),
    pcSpellSlots: r.many.pcSpellSlots({
      from: r.playableCharacters.id,
      to: r.pcSpellSlots.pc_id,
    })
  },
  pcSpellSlots: {
    pcSpells: r.many.pcSpells({
      from: [r.pcSpellSlots.pc_id, r.pcSpellSlots.level],
      to: [r.pcSpells.pc_id, r.pcSpells.level],
    })
  }
}))
