from pydantic import BaseModel


class SetDataChangeDataParams(BaseModel):
    new_data_params: list = ["PARAM_1", "PARAM_2", "PARAM_3", "PARAM_4", "PARAM_5"]
