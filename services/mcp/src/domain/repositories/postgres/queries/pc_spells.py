from domain.entities.spell import PartialSpell, Spell

from .utils import (
    insert_columns,
    insert_placeholders,
    update_placeholders,
)

INSERT = f"""
INSERT INTO pc_spells
    ({insert_columns(Spell)})
VALUES
    ({insert_placeholders(Spell)})
"""


SELECT = """
SELECT * FROM pc_spells
WHERE pc_id = $1
"""


UPDATE = f"""
UPDATE pc_spells
SET
    {update_placeholders(PartialSpell, 2)}
WHERE pc_id = $1 AND name = $2
"""
