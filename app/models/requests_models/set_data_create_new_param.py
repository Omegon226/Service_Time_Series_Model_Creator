from pydantic import BaseModel


class SetDataCreateNewParam(BaseModel):
    type_of_param: str = "mean"
    name_of_new_param: str | None = None
    window_size: int | None = 5
