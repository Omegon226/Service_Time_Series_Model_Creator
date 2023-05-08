from pydantic import BaseModel


class SetDataChangeDataParams(BaseModel):
    new_data_params: list = []