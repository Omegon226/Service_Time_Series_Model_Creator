from pydantic import BaseModel


class SetVisualizeRollingStatisticsOfData(BaseModel):
    window_size: int = 5
    params_for_analyze: str | list = "PARAM_1"
