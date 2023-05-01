from pydantic import BaseModel


class SetDataMainParamRequest(BaseModel):
    parameter_to_set_main: str = "07HAH10CP901"

