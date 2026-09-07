from typing import Any

from pydantic import BaseModel


def insert_placeholders(d: dict[str, Any]) -> str:
    return ", ".join([f"${i + 1}" for i in range(len(d))])


def update_placeholders(d: dict[str, Any], base: int) -> str:
    return ", ".join(
        [f"{key} = COALESCE(${base + i + 1}, {key})" for i, key in enumerate(d)]
    )
