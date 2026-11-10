from pydantic import BaseModel


class SpellBody(BaseModel):
    name: str
    level: int
    prepared: bool


class Spell(SpellBody):
    pc_id: int


class PartialSpell(BaseModel):
    name: str | None = None
    level: int | None = None
    prepared: bool | None = None
