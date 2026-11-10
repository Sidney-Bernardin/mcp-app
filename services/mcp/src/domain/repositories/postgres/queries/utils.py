from pydantic import BaseModel


def insert_placeholders(m: type[BaseModel]) -> str:
    placeholders = [f"${i + 1}" for i in range(len(m.model_fields))]
    return ", ".join(placeholders)


def insert_columns(m: type[BaseModel]) -> str:
    # fmt: off
    return ", ".join([
        v.alias if v.alias is not None else k
        for k, v in m.model_fields.items()
    ])
    # fmt: on


def update_placeholders(m: type[BaseModel], start_number: int) -> str:
    placeholders = []
    for i, (k, v) in enumerate(m.model_fields.items()):
        key = v.alias if v.alias is not None else k
        placeholders.append(f"{key} = COALESCE(${start_number + i}, {key})")

    return ", ".join(placeholders)
