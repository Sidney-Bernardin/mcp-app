from domain.entities.spell_slot import PartialSpellSlot, SpellSlot

from .utils import (
    insert_columns,
    insert_placeholders,
    update_placeholders,
)

INSERT = f"""
INSERT INTO pc_spell_slots
    ({insert_columns(SpellSlot)})
VALUES
    ({insert_placeholders(SpellSlot)})
"""


SELECT = """
SELECT * FROM pc_spell_slots
WHERE pc_id = $1
"""


UPDATE = f"""
UPDATE pc_spell_slots
SET
    {update_placeholders(PartialSpellSlot, 2)}
WHERE pc_id = $1 AND level = $2
"""
