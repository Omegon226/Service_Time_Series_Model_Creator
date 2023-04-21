from pydantic import BaseModel


class SetDataCreateNewParam(BaseModel):
    type_of_param: str = "mean"
    window_size: int | None = 5
