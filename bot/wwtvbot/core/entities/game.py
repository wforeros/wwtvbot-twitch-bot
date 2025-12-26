from pydantic import BaseModel, field_validator


class Game(BaseModel):
    id: str
    name: str

    @field_validator("id", "name")
    def not_empty(cls, v: str) -> str:
        if not v or not v.strip():
            if not v or not v.strip():
                raise ValueError("must not be empty")
        return v
