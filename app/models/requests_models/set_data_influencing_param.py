from pydantic import BaseModel


class SetDataInfluencingParamRequest(BaseModel):
    parameter_to_set_influencing: str = "07HAH10CP901"

