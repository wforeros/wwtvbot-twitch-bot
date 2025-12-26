from pydantic import BaseModel, field_validator


class User(BaseModel):
    id: str
    username: str | None

    @field_validator("id", "username")
    def not_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("must not be empty")
        return v
