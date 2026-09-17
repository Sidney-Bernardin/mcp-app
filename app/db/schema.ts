import { sql } from "drizzle-orm"
import { defineRelations } from "drizzle-orm"
import {
  pgTable, primaryKey, check, foreignKey, unique,
  bytea, text, serial, varchar, integer, boolean, timestamp,
} from "drizzle-orm/pg-core"


export const users = pgTable("users", {
  id: serial().primaryKey(),
  username: varchar({ length: 255 }).notNull(),
  passwordHash: bytea().notNull(),
  passwordSalt: bytea().notNull(),
  createdAt: timestamp().defaultNow().notNull(),
})

export const playableCharacters = pgTable("playable_characters", {
  id: serial().primaryKey(),

  name: text().notNull(),
  class: text().notNull(),
  level: text().notNull(),
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

  strengthMod: text().notNull(),
  dexterityMod: text().notNull(),
  constitutionMod: text().notNull(),
  intelligenceMod: text().notNull(),
  wisdomMod: text().notNull(),
  charismaMod: text().notNull(),

  strengthSv: text().notNull(),
  dexteritySv: text().notNull(),
  constitutionSv: text().notNull(),
  intelligenceSv: text().notNull(),
  wisdomSv: text().notNull(),
  charismaSv: text().notNull(),

  inspiration: text().notNull(),
  proficiencyBonus: text().notNull(),
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
  sleightOfHand: text().notNull(),
  stealth: text().notNull(),
  survival: text().notNull(),

  armorClass: text().notNull(),
  initiative: text().notNull(),
  speed: text().notNull(),

  hpMax: text().notNull(),
  hpCurrent: text().notNull(),

  hpTemp: text().notNull(),
  hitDice: text().notNull(),
  hitDiceTotal: text().notNull(),

  deathSavesSuccesses: text().notNull(),
  deathSavesFailures: text().notNull(),

  spellCastAbility: text().notNull(),
  spellSaveDc: text().notNull(),
  spellAttackBonus: text().notNull(),

  spellSlotTotal: integer().array().default(sql`ARRAY[0, 0, 0, 0, 0, 0, 0, 0, 0]`),
  spellSlotExpended: integer().array().default(sql`ARRAY[0, 0, 0, 0, 0, 0, 0, 0, 0]`),

  otherProficienciesAndLanguages: text().array().notNull(),
  equipment: text().array().notNull(),
  featuresAndTraits: text().array().notNull(),

  copper: text().notNull(),
  silver: text().notNull(),
  emerald: text().notNull(),
  gold: text().notNull(),
  platinum: text().notNull(),
}, (table) => [
  check("spell_slot_total_check", sql`cardinality(${table.spellSlotTotal}) = 9`)
])

export const pcAttacks = pgTable("pc_attacks", {
  pcId: serial().references(() => playableCharacters.id),
  name: text().notNull(),

  bonus: text().notNull(),
  damage: text().notNull(),
  type: text().notNull(),
}, (table) => [
  primaryKey({ columns: [table.pcId, table.name] })
])

export const pcSpellSlots = pgTable("pc_spell_slots", {
  pcId: serial().notNull(),
  level: text().notNull(),

  total: text().notNull(),
  expended: text().notNull(),
}, (table) => [
  primaryKey({ columns: [table.pcId, table.level] }),
])

export const pcSpells = pgTable("pc_spells", {
  pcId: serial(),
  name: text().notNull(),

  level: text(),
  prepared: boolean().notNull(),
}, (table) => [
  primaryKey({ columns: [table.pcId, table.level] }),
  foreignKey({
    columns: [table.pcId, table.level],
    foreignColumns: [pcSpellSlots.pcId, pcSpellSlots.level],
  }),
])

export const relations = defineRelations({ playableCharacters, pcAttacks, pcSpellSlots, pcSpells }, (r) => ({
  playableCharacters: {
    pcAttacks: r.many.pcAttacks({
      from: r.playableCharacters.id,
      to: r.pcAttacks.pcId,
    }),
    pcSpellSlots: r.many.pcSpellSlots({
      from: r.playableCharacters.id,
      to: r.pcSpellSlots.pcId,
    })
  },
  pcSpellSlots: {
    pcSpells: r.many.pcSpells({
      from: [r.pcSpellSlots.pcId, r.pcSpellSlots.level],
      to: [r.pcSpells.pcId, r.pcSpells.level],
    })
  }
}))
