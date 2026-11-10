from domain.entities.playable_character import (
    PartialPlayableCharacter,
    PlayableCharacterBody,
)
from domain.repositories.postgres.queries.utils import (
    insert_columns,
    insert_placeholders,
    update_placeholders,
)

INSERT = f"""
INSERT INTO playable_characters
    ({insert_columns(PlayableCharacterBody)})
VALUES
    ({insert_placeholders(PlayableCharacterBody)})
RETURNING id
"""


SELECT = """
SELECT * FROM playable_characters
WHERE id = $1
"""


UPDATE = f"""
UPDATE playable_characters
SET
    {update_placeholders(PartialPlayableCharacter, 2)}
WHERE id = $1
"""
