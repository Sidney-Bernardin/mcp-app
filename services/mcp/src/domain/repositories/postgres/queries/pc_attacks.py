from domain.entities.attack import Attack, PartialAttack

from .utils import (
    insert_columns,
    insert_placeholders,
    update_placeholders,
)

INSERT = f"""
INSERT INTO pc_attacks
    ({insert_columns(Attack)})
VALUES
    ({insert_placeholders(Attack)})
"""


SELECT = """
SELECT * FROM pc_attacks
WHERE pc_id = $1
"""


UPDATE = f"""
UPDATE pc_attacks
SET
    {update_placeholders(PartialAttack, 2)}
WHERE pc_id = $1 AND name = $2
"""
