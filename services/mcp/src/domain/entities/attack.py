from pydantic import BaseModel


class AttackBody(BaseModel):
    name: str
    bonus: str
    damage: str
    type: str


class Attack(AttackBody):
    pc_id: int


class PartialAttack(BaseModel):
    name: str | None = None
    bonus: str | None = None
    damage: str | None = None
    type: str | None = None
