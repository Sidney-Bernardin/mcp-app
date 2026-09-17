from pydantic import BaseModel


class Matter(BaseModel):
    mass: int


class Animal(BaseModel):
    name: str


class Person(Animal, Matter):
    last_name: str


p = Person(name="sidney", last_name="bernardin", mass=10)
print(p.__class__.__base__)
