import { db } from "@/db"
import { playableCharacters } from "@/db/schema";

export default async function Home() {
  const pc: typeof playableCharacters.$inferInsert = {
    name: "abc",
    class: "abc",
    level: "abc",
    background: "abc",
    race: "abc",
    alignment: "abc",
    xp: "abc",

    age: "abc",
    height: "abc",
    wight: "abc",
    eyes: "abc",
    skin: "abc",
    hair: "abc",

    strength: "abc",
    dexterity: "abc",
    constitution: "abc",
    intelligence: "abc",
    wisdom: "abc",
    charisma: "abc",

    strengthMod: "abc",
    dexterityMod: "abc",
    constitutionMod: "abc",
    intelligenceMod: "abc",
    wisdomMod: "abc",
    charismaMod: "abc",

    strengthSv: "abc",
    dexteritySv: "abc",
    constitutionSv: "abc",
    intelligenceSv: "abc",
    wisdomSv: "abc",
    charismaSv: "abc",

    inspiration: "abc",
    proficiencyBonus: "abc",
    perseption: "abc",

    acrobatics: "abc",
    animal: "abc",
    arcana: "abc",
    athletics: "abc",
    deception: "abc",
    history: "abc",
    insight: "abc",
    intimidation: "abc",
    investigation: "abc",
    medicine: "abc",
    nature: "abc",
    perception: "abc",
    performance: "abc",
    persuasion: "abc",
    religion: "abc",
    sleightOfHand: "abc",
    stealth: "abc",
    survival: "abc",

    armorClass: "abc",
    initiative: "abc",
    speed: "abc",

    hpMax: "abc",
    hpCurrent: "abc",

    hpTemp: "abc",
    hitDice: "abc",
    hitDiceTotal: "abc",

    deathSavesSuccesses: "abc",
    deathSavesFailures: "abc",

    spellCastAbility: "abc",
    spellSaveDc: "abc",
    spellAttackBonus: "abc",

    spellSlotTotal: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    spellSlotExpended: [0, 0, 0, 0, 0, 0, 0, 0, 0],

    otherProficienciesAndLanguages: ["abc"],
    equipment: ["abc"],
    featuresAndTraits: ["abc"],

    copper: "abc",
    silver: "abc",
    emerald: "abc",
    gold: "abc",
    platinum: "abc",
  }
  const x = await db.insert(playableCharacters).values(pc)
  console.log(x)

  const y = await db.query.playableCharacters.findFirst({
    with: {
      pcAttacks: true,
      pcSpellSlots: {
        with: {
          pcSpells: true,
        }
      },
    }
  })
  console.log(y)

  return (
    <div className="">
      <h2>home</h2>
    </div>
  );
}
