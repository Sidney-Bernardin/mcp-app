from pydantic import BaseModel


class Person(BaseModel):
    name: str = []


p = Person()
print(p)
