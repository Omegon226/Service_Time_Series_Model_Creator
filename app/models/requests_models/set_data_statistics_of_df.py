from pydantic import BaseModel
from typing import Union


class SetDataStatisticsOfDf(BaseModel):
    params_statistics: Union[list, str] = ["PARAM_1", "PARAM_2", "PARAM_3", "PARAM_4", "PARAM_5"]
