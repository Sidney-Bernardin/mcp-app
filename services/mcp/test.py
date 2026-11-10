from pydantic import BaseModel, ConfigDict


# class BaseWithExtra(BaseModel):
#     inherited_field: str
#
#
# class SourceModel(BaseWithExtra):
#     id: int
#     name: str
#
#
# class TargetModel(BaseModel):
#     # model_config = ConfigDict(extra="allow")  # Causes extra fields to stick!
#     id: int
#     name: str
#
# source = SourceModel(id=1, name="Alice", inherited_field="should be ignored")
#
# # Force source to only dump keys that TargetModel explicitly defines
# target = TargetModel.model_validate(
#     source.model_dump(
#         # include=set(TargetModel.model_fields.keys())
#     )
# )
#
# print(target.model_dump())
# # Output: {'id': 1, 'name': 'Alice'}


class PersonHead(BaseModel):
    id: int


class PersonBody(BaseModel):
    name: str
    age: int


class Person(PersonHead, PersonBody):
    pass


person = Person(id=1, name="bob", age=30)
person_body = PersonBody.model_validate(person, from_attributes=True)
print(person_body)
