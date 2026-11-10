from pydantic import BaseModel


class SpellSlotBody(BaseModel):
    level: int
    total: str
    expended: str


class SpellSlot(SpellSlotBody):
    pc_id: int


class PartialSpellSlot(BaseModel):
    level: int | None = None
    total: str | None = None
    expended: str | None = None
