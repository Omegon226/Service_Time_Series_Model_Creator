from pydantic import BaseModel


class SetDataChangeNan(BaseModel):
    type_of_editing: str = "zero"
    window_size: str | None = 5
